# Escrow specification
Created -> Funded or Cancelled. Funded -> Released or Disputed. Disputed ->
ResolvedToBuyer or ResolvedToSeller. Terminal states permit no further transitions.
Buyer alone funds and releases; buyer or seller may dispute; arbiter alone resolves.
Cancellation requires both buyer and seller agreement before funding. Funds are allocated
as pull-payment credits; withdrawal uses checks-effects-interactions and a reentrancy guard.
