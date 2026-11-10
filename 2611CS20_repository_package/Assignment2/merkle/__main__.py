import argparse,json
from . import root,prove,verify
p=argparse.ArgumentParser(); s=p.add_subparsers(dest="cmd",required=True)
for c in ("root","prove","verify"):
 q=s.add_parser(c); q.add_argument("file")
 if c=="prove": q.add_argument("index",type=int)
 if c=="verify": q.add_argument("proof"); q.add_argument("root")
a=p.parse_args(); items=[x.encode() for x in json.load(open(a.file))]
if a.cmd=="root": print(root(items).hex())
elif a.cmd=="prove": print(json.dumps(prove(items,a.index),indent=2))
else:
 pr=json.load(open(a.proof)); print("VALID" if verify(items[pr["leaf_index"]],pr,a.root) else "INVALID")
