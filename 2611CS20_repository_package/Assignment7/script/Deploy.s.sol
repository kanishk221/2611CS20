// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "forge-std/Script.sol";
import "../src/Escrow.sol";
contract Deploy is Script {
 function run() external returns(Escrow e) {
  uint256 key=vm.envUint("PRIVATE_KEY"); address buyer=vm.envAddress("BUYER");
  address seller=vm.envAddress("SELLER"); address arbiter=vm.envAddress("ARBITER");
  uint256 amount=vm.envUint("ESCROW_AMOUNT");
  vm.startBroadcast(key); e=new Escrow(buyer,seller,arbiter,amount); vm.stopBroadcast();
 }
}
