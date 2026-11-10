from wallet import *
def test_signature_and_canonical():
 tx={"version":1,"network_id":"course-testnet","sender":"a","recipient":"b","amount_units":10,"nonce":1,"memo_hash":"00"}
 k=Ed25519PrivateKey.generate()
 pub=k.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw)
 sig=k.sign(canonical(tx)); assert verify(tx,pub,sig)
 tx["amount_units"]=11; assert not verify(tx,pub,sig)
