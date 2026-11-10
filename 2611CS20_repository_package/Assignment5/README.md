# Assignment 5 — toy proof-of-work chain
Implements deterministic block headers, SHA-256 proof of work, cumulative-work chain selection,
and a two-branch fork demonstration. Target is an integer threshold; smaller targets are harder.
This compact teaching model focuses on header hashing and chain selection; transaction/UTXO
validation is represented by a caller-supplied block validity flag. Run `python -m chain` and `pytest`.
