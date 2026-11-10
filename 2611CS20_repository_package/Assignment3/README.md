# Assignment 3 — educational Ed25519 wallet
Uses `cryptography` Ed25519 backed by OS randomness. Addresses are Base58Check of
version byte 0x00 + RIPEMD160(SHA256(public key)); checksum is first four bytes of double SHA-256.
Transaction bytes are UTF-8 canonical JSON: sorted keys, compact separators, ASCII escaping disabled.
Nonce replay protection is represented by the verifier's caller-supplied minimum/used nonce.
This is an educational testnet wallet, not production wallet software.
Commands: `python -m wallet keygen DIR`, `address PUB`, `sign TX PRIVATE`, `verify TX PUB SIG`.
Tests: `pytest`.
