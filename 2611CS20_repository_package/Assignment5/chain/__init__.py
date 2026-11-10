import hashlib,json,time
def header_bytes(h): return json.dumps(h,sort_keys=True,separators=(",",":")).encode()
def hash_header(h): return hashlib.sha256(header_bytes(h)).digest()
def mine(header,target,max_nonce=10_000_000):
 h=dict(header)
 for n in range(max_nonce):
  h["nonce"]=n; d=hash_header(h)
  if int.from_bytes(d,"big")<=target: return h,d.hex(),n+1
 raise RuntimeError("nonce search exhausted")
def work(target): return (1<<256)//(target+1)
class Chain:
 def __init__(self): self.blocks={}
 def add(self,block):
  if not block.get("valid",False): raise ValueError("invalid block")
  if block["prev"] and block["prev"] not in self.blocks: raise ValueError("unknown parent")
  if int(block["hash"],16)>block["target"]: raise ValueError("invalid proof of work")
  self.blocks[block["hash"]]=block
 def best_tip(self):
  def score(h):
   s=0
   while h:
    b=self.blocks[h]; s+=work(b["target"]); h=b["prev"]
   return s
  return max(self.blocks,key=score) if self.blocks else None
