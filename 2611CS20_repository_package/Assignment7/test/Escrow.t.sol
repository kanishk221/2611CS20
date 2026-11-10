// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "forge-std/Test.sol";
import "../src/Escrow.sol";
contract EscrowTest is Test {
 address b=address(1); address s=address(2); address a=address(3); Escrow e;
 function setUp() public {e=new Escrow(b,s,a,1 ether); vm.deal(b,5 ether);}
 function testFundReleaseWithdraw() public {
  vm.prank(b); e.fund{value:1 ether}(); vm.prank(b); e.release();
  assertEq(e.credits(s),1 ether); vm.prank(s); e.withdraw(); assertEq(e.totalLiability(),0);
 }
 function testDisputeArbiterBuyerRefund() public {
  vm.prank(b); e.fund{value:1 ether}(); vm.prank(s); e.dispute();
  vm.prank(a); e.resolve(false); assertEq(e.credits(b),1 ether);
 }
 function testUnauthorizedRelease() public {
  vm.prank(b); e.fund{value:1 ether}(); vm.prank(s); vm.expectRevert(Escrow.Unauthorized.selector); e.release();
 }
 function testMutualCancel() public {
  vm.prank(b); e.agreeCancel(); vm.prank(s); e.agreeCancel(); assertEq(uint(e.state()),uint(Escrow.State.Cancelled));
 }
}
