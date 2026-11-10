# Assignment 7 — Solidity escrow
Foundry project. Install Foundry, then run `forge test`. Local deployment:
`anvil` in one terminal; `forge script script/Deploy.s.sol --rpc-url http://127.0.0.1:8545 --broadcast`.
Escrow roles: buyer funds, buyer releases, buyer or seller opens dispute, arbiter resolves,
and buyer+seller mutually cancel only while Created. Payouts use pull-payment withdrawals.
