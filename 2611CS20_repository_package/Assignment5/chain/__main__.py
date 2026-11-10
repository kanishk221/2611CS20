from . import *
target=(1<<248)-1
h={"version":1,"prev":"","merkle_root":"00"*32,"timestamp":int(time.time()),"target":target,"nonce":0}
b,d,tries=mine(h,target); print("block hash:",d,"attempts:",tries)
