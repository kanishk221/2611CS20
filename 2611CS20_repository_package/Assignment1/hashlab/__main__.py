import argparse, base64, hashlib, json, sys
from pathlib import Path

def digest_stream(stream, chunk_size=1024*1024):
    h=hashlib.sha256(); size=0
    while True:
        chunk=stream.read(chunk_size)
        if not chunk: break
        size += len(chunk); h.update(chunk)
    return size, h.digest()

def report(data):
    d=hashlib.sha256(data).digest()
    print(f"bytes: {len(data)}")
    print(f"sha256: {d.hex()}")
    print(f"base64: {base64.b64encode(d).decode()}")

def main():
    p=argparse.ArgumentParser(prog="hashlab"); sub=p.add_subparsers(dest="cmd",required=True)
    t=sub.add_parser("text"); t.add_argument("value")
    x=sub.add_parser("hex"); x.add_argument("value")
    f=sub.add_parser("file"); f.add_argument("path")
    a=sub.add_parser("avalanche"); a.add_argument("--text",required=True); a.add_argument("--bit",type=int,required=True)
    c=sub.add_parser("canonical-json"); c.add_argument("path")
    args=p.parse_args()
    if args.cmd=="text": report(args.value.encode("utf-8"))
    elif args.cmd=="hex":
        try: data=bytes.fromhex(args.value)
        except ValueError: p.error("malformed hexadecimal input")
        report(data)
    elif args.cmd=="file":
        with open(args.path,"rb") as stream:
            size,d=digest_stream(stream)
        print(f"bytes: {size}\nsha256: {d.hex()}\nbase64: {base64.b64encode(d).decode()}")
    elif args.cmd=="avalanche":
        data=bytearray(args.text.encode()); bit=args.bit
        if bit<0 or bit>=len(data)*8: p.error("bit index outside input")
        changed=bytearray(data); changed[bit//8] ^= 1 << (7-bit%8)
        d1=hashlib.sha256(data).digest(); d2=hashlib.sha256(changed).digest()
        print(f"changed_bits_in_digest: {sum((u^v).bit_count() for u,v in zip(d1,d2))}")
    else:
        obj=json.loads(Path(args.path).read_text(encoding="utf-8"))
        if not isinstance(obj,dict): p.error("canonical-json requires a JSON object")
        data=json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
        report(data)
if __name__=="__main__": main()
