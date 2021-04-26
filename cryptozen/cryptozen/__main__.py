from cryptozen.Transposition import Transpose
from cryptozen.Ceaser_Cipher import Ceaser
import sys
import os

done = False
try:
    if sys.argv[1] == "--ceaser":
        print(Ceaser().encrypt())
        done = True
except:
    print("Usage 'python -m cryptozen --ceaser'")

if done:
    sys.exit()

try:
    if sys.argv[1] == "--transpose" and int(sys.argv[2]):
        print(Transpose(key=int(sys.argv[2])).encrypt())
    else:
        print("Usage 'python -m cryptozen --transpose 12(any number)'")
    done = True
except:
    print("Usage 'python -m cryptozen --transpose 12(any number)'")

if done:
    sys.exit()
