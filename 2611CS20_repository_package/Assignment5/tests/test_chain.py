from chain import *
def test_mine_and_most_work():
 t=(1<<255)-1; h={"version":1,"prev":"","merkle_root":"00"*32,"timestamp":1,"target":t}
 b,d,_=mine(h,t); c=Chain(); c.add({"hash":d,"target":t,"prev":"","valid":True})
 assert c.best_tip()==d
