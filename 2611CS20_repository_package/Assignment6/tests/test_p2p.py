import socket,threading
from p2p import *
def test_frame_and_dedup():
 a,b=socket.socketpair(); a.sendall(encode({"version":1,"type":"ping"})); assert recv_message(b)["type"]=="ping"
 n=Node("a"); m={"version":1,"type":"tx","id":"abc","payload":{}}
 assert n.handle(m)["type"]=="inv"; assert n.handle(m)["type"]=="duplicate"
