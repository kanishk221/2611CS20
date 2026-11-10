# Transaction byte format
Required fields: version (integer), network_id (string), sender (address), recipient (address),
amount_units (non-negative integer), nonce (non-negative integer), memo_hash (hex string).
Serialization: UTF-8 JSON; keys sorted lexicographically; separators `,` and `:`; Unicode unescaped;
NaN/Infinity forbidden. Ed25519 signs these exact bytes. Whitespace and input key order do not matter.
