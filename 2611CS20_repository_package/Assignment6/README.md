# Assignment 6 — localhost P2P relay prototype
A length-prefixed JSON TCP peer that enforces a maximum frame size, handshake version,
duplicate suppression, ping/pong and structured logs. Start a node with `python -m p2p PORT`.
Connect another node with `python -m p2p PORT --peer HOST:PORT`. Run `pytest`.
This is a minimal transport prototype; production peer scoring, fee-rate mempool policy,
partition simulation and chain convergence require integration with Assignment 5.
