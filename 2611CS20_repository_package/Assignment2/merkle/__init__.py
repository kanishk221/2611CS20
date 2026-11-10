import hashlib, json
def leaf(data: bytes)->bytes: return hashlib.sha256(b"\x00"+data).digest()
def node(left: bytes,right: bytes)->bytes: return hashlib.sha256(b"\x01"+left+right).digest()
def levels(items):
    cur=[leaf(x) for x in items]
    if not cur: return [[hashlib.sha256(b"").digest()]]
    out=[cur]
    while len(cur)>1:
        nxt=[]
        for i in range(0,len(cur),2):
            nxt.append(node(cur[i],cur[i+1]) if i+1<len(cur) else cur[i])
        out.append(nxt); cur=nxt
    return out
def root(items): return levels(items)[-1][0]
def prove(items,index):
    ls=levels(items)
    if index<0 or index>=len(items): raise IndexError("leaf index out of range")
    proof=[]; idx=index
    for level in ls[:-1]:
        sib=idx^1
        if sib<len(level): proof.append({"side":"left" if sib<idx else "right","hash":level[sib].hex()})
        else: proof.append({"side":"promote"})
        idx//=2
    return {"leaf_index":index,"tree_size":len(items),"siblings":proof}
def verify(data,proof,expected_root):
    try:
        idx=proof["leaf_index"]; size=proof["tree_size"]; steps=proof["siblings"]
        if not isinstance(idx,int) or not isinstance(size,int) or size<1 or idx<0 or idx>=size: return False
        expected_steps=0; n=size
        while n>1: expected_steps+=1; n=(n+1)//2
        if len(steps)!=expected_steps: return False
        h=leaf(data); pos=idx; width=size
        for step in steps:
            side=step["side"]
            if side=="promote" and pos%2==0 and pos+1==width: pass
            else:
                sh=bytes.fromhex(step["hash"])
                if len(sh)!=32: return False
                if side=="left" and pos%2==1: h=node(sh,h)
                elif side=="right" and pos%2==0 and pos+1<width: h=node(h,sh)
                else: return False
            pos//=2; width=(width+1)//2
        return h.hex()==expected_root
    except (KeyError,TypeError,ValueError): return False
