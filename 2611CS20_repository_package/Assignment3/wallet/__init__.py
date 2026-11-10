import base64,hashlib,json,os
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
ALPH="123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
def b58(b):
 n=int.from_bytes(b,"big"); s=""
 while n: n,r=divmod(n,58); s=ALPH[r]+s
 pad=len(b)-len(b.lstrip(b"\\0")); return "1"*pad+(s or ("" if pad else "1"))
def address(pub):
 h=hashlib.new("ripemd160",hashlib.sha256(pub).digest()).digest()
 payload=b"\x00"+h; chk=hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
 return b58(payload+chk)
def canonical(tx): return json.dumps(tx,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def keygen(directory):
 d=Path(directory); d.mkdir(parents=True,exist_ok=True); k=Ed25519PrivateKey.generate()
 priv=k.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption())
 pub=k.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw)
 (d/"private.test-only.key").write_bytes(priv); os.chmod(d/"private.test-only.key",0o600)
 (d/"public.key").write_bytes(pub); return pub
def sign(tx,priv): return Ed25519PrivateKey.from_private_bytes(priv).sign(canonical(tx))
def verify(tx,pub,sig):
 try:
  from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
  Ed25519PublicKey.from_public_bytes(pub).verify(sig,canonical(tx)); return True
 except Exception: return False
