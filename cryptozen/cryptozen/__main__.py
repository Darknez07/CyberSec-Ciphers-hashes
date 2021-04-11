from cryptozen.Transposition import Transpose
from cryptozen import Ceaser_Cipher
from cryptozen import Files
import sys
import os

try:
    if sys.argv[1] == "--ceaser":
        print(Ceaser_Cipher.encrpyt())
except:
    print("Usage 'python -m cryptozen --ceaser'")
try:
    if sys.argv[1] == "--file":
        if os.path.exists(sys.argv[2]):
            print(Files.Files().use_files(filename=sys.argv[2]))
        else:
            print("Filename wrong")
except:
    print("Usage 'python -m cryptozen --file filename.txt'")

try:
    if sys.argv[1] == "--transpose" and int(sys.argv[2]):
        print(Transpose(key=int(sys.argv[2])).encrypt())
    else:
        print("Usage 'python -m cryptozen --transpose 12(any number)'")
except:
    print("Usage 'python -m cryptozen --transpose 12(any number)'")
