// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
contract Escrow {
 enum State { Created, Funded, Released, Disputed, ResolvedToBuyer, ResolvedToSeller, Cancelled }
 address public immutable buyer; address public immutable seller; address public immutable arbiter;
 uint256 public immutable amount; State public state;
 bool public buyerCancel; bool public sellerCancel;
 mapping(address=>uint256) public credits;
 uint256 public totalLiability;
 error Unauthorized(); error InvalidState(); error WrongValue(); error Reentrant(); error ZeroAddress();
 event FundedEvent(uint256 amount); event DisputedEvent(address indexed by);
 event ResolvedEvent(State outcome); event Withdrawal(address indexed to,uint256 amount);
 uint256 private lock=1;
 modifier nonReentrant(){if(lock!=1) revert Reentrant(); lock=2; _; lock=1;}
 modifier onlyBuyer(){if(msg.sender!=buyer) revert Unauthorized(); _;}
 modifier onlyArbiter(){if(msg.sender!=arbiter) revert Unauthorized(); _;}
 constructor(address b,address s,address a,uint256 v){
  if(b==address(0)||s==address(0)||a==address(0)) revert ZeroAddress();
  if(b==s||b==a||s==a) revert Unauthorized();
  buyer=b;seller=s;arbiter=a;amount=v;
 }
 function fund() external payable onlyBuyer {
  if(state!=State.Created) revert InvalidState(); if(msg.value!=amount||amount==0) revert WrongValue();
  state=State.Funded; totalLiability+=msg.value; emit FundedEvent(msg.value);
 }
 function release() external onlyBuyer {if(state!=State.Funded) revert InvalidState(); state=State.Released; _credit(seller,amount);}
 function dispute() external {if(msg.sender!=buyer&&msg.sender!=seller) revert Unauthorized(); if(state!=State.Funded) revert InvalidState(); state=State.Disputed; emit DisputedEvent(msg.sender);}
 function resolve(bool paySeller) external onlyArbiter {
  if(state!=State.Disputed) revert InvalidState();
  if(paySeller){state=State.ResolvedToSeller;_credit(seller,amount);}
  else {state=State.ResolvedToBuyer;_credit(buyer,amount);}
  emit ResolvedEvent(state);
 }
 function agreeCancel() external {
  if(state!=State.Created) revert InvalidState();
  if(msg.sender==buyer) buyerCancel=true; else if(msg.sender==seller) sellerCancel=true; else revert Unauthorized();
  if(buyerCancel&&sellerCancel) state=State.Cancelled;
 }
 function _credit(address to,uint256 v) private {credits[to]+=v;}
 function withdraw() external nonReentrant {
  uint256 v=credits[msg.sender]; if(v==0) revert WrongValue();
  credits[msg.sender]=0; totalLiability-=v;
  (bool ok,)=msg.sender.call{value:v}(""); require(ok,"transfer failed");
  emit Withdrawal(msg.sender,v);
 }
}
