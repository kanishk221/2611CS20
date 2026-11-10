import argparse,socket,threading
from . import *
def serve(conn,node):
 try:
  conn.sendall(encode({"version":1,"type":"handshake","node_id":node.node_id}))
  while True:
   msg=recv_message(conn); reply=node.handle(msg); conn.sendall(encode(reply))
 except Exception: conn.close()
p=argparse.ArgumentParser(); p.add_argument("port",type=int); p.add_argument("--peer")
a=p.parse_args(); node=Node(str(a.port)); server=socket.socket(); server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); server.bind(("127.0.0.1",a.port)); server.listen()
if a.peer:
 host,port=a.peer.split(":"); s=socket.create_connection((host,int(port))); s.sendall(encode({"version":1,"type":"ping"})); print(recv_message(s))
print(f"node {node.node_id} listening")
while True:
 c,_=server.accept(); threading.Thread(target=serve,args=(c,node),daemon=True).start()
