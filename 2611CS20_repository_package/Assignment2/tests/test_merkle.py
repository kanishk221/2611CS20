from merkle import *
def test_sizes_and_proofs():
 for n in (1,2,5,8,17):
  xs=[f"tx{i}".encode() for i in range(n)]
  for i,x in enumerate(xs): assert verify(x,prove(xs,i),root(xs).hex())
def test_tamper():
 xs=[b"a",b"b",b"c"]; p=prove(xs,1); p["siblings"][0]["hash"]="00"*32
 assert not verify(xs[1],p,root(xs).hex())
