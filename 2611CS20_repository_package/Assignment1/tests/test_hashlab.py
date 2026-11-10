import hashlib, io
from hashlab import __main__ as h

def test_stream():
    data=b"x"*2_000_000
    n,d=h.digest_stream(io.BytesIO(data),8192)
    assert n==len(data) and d==hashlib.sha256(data).digest()

def test_newline_changes_hash():
    assert hashlib.sha256(b"hello").digest()!=hashlib.sha256(b"hello\n").digest()
