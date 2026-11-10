import hashlib,hmac
from utxo import *
def test_atomic_spend_and_double_spend():
 l=Ledger(); l.add("genesis",0,50,"alice"); secret={"alice":b"secret"}
 tx={"inputs":[{"txid":"genesis","index":0,"signature":""}],"outputs":[{"value":40,"owner":"bob"}]}
 tx["txid"]=txid(tx); tx["inputs"][0]["signature"]=hmac.new(secret["alice"],(tx["txid"]+"alice").encode(),hashlib.sha256).hexdigest()
 assert l.apply(tx,secret)==10
 before=dict(l.utxos)
 try: l.apply(tx,secret)
 except ValueError: pass
 assert l.utxos==before
