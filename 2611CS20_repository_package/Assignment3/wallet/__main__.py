import argparse,json
from pathlib import Path
from . import *
p=argparse.ArgumentParser(); s=p.add_subparsers(dest="cmd",required=True)
k=s.add_parser("keygen"); k.add_argument("directory")
a=s.add_parser("address"); a.add_argument("public")
sg=s.add_parser("sign"); sg.add_argument("tx"); sg.add_argument("private")
v=s.add_parser("verify"); v.add_argument("tx"); v.add_argument("public"); v.add_argument("signature")
x=p.parse_args()
if x.cmd=="keygen": print("address:",address(keygen(x.directory)).__str__())
elif x.cmd=="address": print(address(Path(x.public).read_bytes()))
elif x.cmd=="sign": print(sign(json.load(open(x.tx)),Path(x.private).read_bytes()).hex())
else: print("VALID" if verify(json.load(open(x.tx)),Path(x.public).read_bytes(),bytes.fromhex(x.signature)) else "INVALID")
