import hashlib,hmac,json
MAX=(1<<64)-1
def txid(tx): return hashlib.sha256(json.dumps(tx,sort_keys=True,separators=(",",":")).encode()).hexdigest()
class Ledger:
 def __init__(self): self.utxos={}
 def add(self,tid,index,value,owner):
  if not 0<=value<=MAX: raise ValueError("output value out of range")
  self.utxos[(tid,index)]={"value":value,"owner":owner}
 def apply(self,tx,secret_by_owner):
  seen=set(); total_in=0
  for i in tx["inputs"]:
   op=(i["txid"],i["index"])
   if op in seen: raise ValueError("duplicate input")
   seen.add(op)
   if op not in self.utxos: raise ValueError("missing or already spent outpoint")
   u=self.utxos[op]; owner=u["owner"]
   msg=(tx["txid"]+owner).encode()
   expected=hmac.new(secret_by_owner[owner],msg,hashlib.sha256).hexdigest()
   if not hmac.compare_digest(expected,i["signature"]): raise ValueError("bad signature")
   total_in+=u["value"]
   if total_in>MAX: raise ValueError("input overflow")
  total_out=0
  for o in tx["outputs"]:
   if not isinstance(o["value"],int) or o["value"]<0 or o["value"]>MAX: raise ValueError("output value out of range")
   total_out+=o["value"]
   if total_out>MAX: raise ValueError("output overflow")
  if total_in<total_out: raise ValueError("inputs less than outputs")
  # Commit only after all checks pass.
  tid=txid(tx)
  for op in seen: del self.utxos[op]
  for n,o in enumerate(tx["outputs"]): self.utxos[(tid,n)]={"value":o["value"],"owner":o["owner"]}
  return total_in-total_out
 def save(self,path):
  json.dump([{"txid":k[0],"index":k[1],**v} for k,v in sorted(self.utxos.items())],open(path,"w"),sort_keys=True)
 def load(self,path):
  self.utxos={}
  for x in json.load(open(path)): self.utxos[(x["txid"],x["index"])]={"value":x["value"],"owner":x["owner"]}
def select_coins(utxos,target):
 chosen=[]; total=0
 for op,u in sorted(utxos.items(),key=lambda kv:(-kv[1]["value"],kv[0])):
  chosen.append((op,u)); total+=u["value"]
  if total>=target: return chosen,total
 raise ValueError("insufficient funds")
