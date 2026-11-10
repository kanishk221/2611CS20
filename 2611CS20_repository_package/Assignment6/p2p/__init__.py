import json,struct,socket,threading,time
MAX_MESSAGE=1_000_000
def encode(msg):
 b=json.dumps(msg,separators=(",",":")).encode()
 if len(b)>MAX_MESSAGE: raise ValueError("message too large")
 return struct.pack("!I",len(b))+b
def recv_exact(sock,n):
 out=b""
 while len(out)<n:
  part=sock.recv(n-len(out))
  if not part: raise ConnectionError("peer disconnected")
  out+=part
 return out
def recv_message(sock):
 n=struct.unpack("!I",recv_exact(sock,4))[0]
 if n>MAX_MESSAGE: raise ValueError("frame exceeds maximum")
 return json.loads(recv_exact(sock,n))
class Node:
 def __init__(self,node_id): self.node_id=node_id; self.seen=set(); self.mempool={}; self.logs=[]
 def handle(self,msg,peer="local"):
  if msg.get("version")!=1: raise ValueError("unsupported protocol version")
  typ=msg.get("type")
  if typ=="ping": return {"version":1,"type":"pong"}
  if typ in ("tx","block"):
   oid=msg.get("id")
   if not oid: raise ValueError("missing object id")
   if oid in self.seen: return {"version":1,"type":"duplicate"}
   self.seen.add(oid)
   if typ=="tx": self.mempool[oid]=msg.get("payload")
   self.logs.append({"node_id":self.node_id,"peer_id":peer,"object_id":oid,"event":"accepted_"+typ,"timestamp":time.time()})
   return {"version":1,"type":"inv","id":oid,"object_type":typ}
  raise ValueError("unknown message type")
