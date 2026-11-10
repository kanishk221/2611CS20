# Assignment 4 — UTXO ledger
In-memory UTXO model with P2PKH-style ownership, deterministic largest-first coin selection,
atomic validation/update and JSON persistence. Values are bounded to unsigned 64-bit integers.
This educational ledger uses HMAC signatures for deterministic local tests; replace with public-key
signatures when integrating Assignment 3. Run `pytest`.
