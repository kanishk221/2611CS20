# Threat model
- Key theft: restrict private-key file permissions; never commit private keys; use hardware-backed storage in real systems.
- Weak randomness: rely on the cryptography library and OS CSPRNG; never seed a PRNG manually.
- Replay: include network ID and nonce; production nodes must persist nonce state.
- Clipboard replacement: verify recipient address on a trusted display.
- Phishing: verify software distribution and transaction details.
- Mainnet accidents: hard-code a clearly named course-testnet domain and never reuse keys on mainnet.
