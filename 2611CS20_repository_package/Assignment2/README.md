# Assignment 2 — Merkle trees
Domain separation: leaf = SHA256(0x00 || data), node = SHA256(0x01 || left || right).
An unpaired final node is promoted unchanged to the next level (no duplicate-last rule).
Proof entries specify sibling side. Empty tree root is SHA256(empty); single leaf root is its leaf hash.
Run `python -m pip install -r requirements.txt`, then `python -m merkle root input.json`.
Input is a JSON array of strings. Commands: root, prove, verify. Tests: `pytest`.
