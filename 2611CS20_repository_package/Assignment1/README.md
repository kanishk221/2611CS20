# Assignment 1 — hashlab
Python 3.11+. Implements text, hex, file, avalanche and canonical JSON SHA-256 diagnostics.
Run: `python -m pip install -r requirements.txt`; `python -m hashlab text "Alice pays Bob 10"`.
For file streaming: `python -m hashlab file path/to/file`.
Canonical JSON rules: UTF-8, sorted object keys, no insignificant whitespace, ensure_ascii=False,
and JSON numbers/strings retain their types. Arrays preserve order. SHA-256 is provided by hashlib.
Avalanche bit indexes are zero-based, most-significant-bit first within each byte.
Tests: `python -m pytest`.
