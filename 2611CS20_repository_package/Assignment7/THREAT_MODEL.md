# Threat model
Role overlap and zero addresses are rejected. Unauthorized state transitions revert.
Only the exact agreed amount is accepted. Payouts are pull-based; withdrawal clears liability
before the external call and is guarded against reentrancy. Arbiter is trusted to resolve disputes.
Production deployment should add governance/arbiter replacement policy, timeouts, and audits.
