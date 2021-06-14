from cryptozen.Transposition import Transpose
from cryptozen.Ceaser_Cipher import Ceaser,letters
from cryptozen import Files
import os
import argparse
#shift to argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ceaser',action='store',type=int,help='Ceaser cipher with specified number')
parser.add_argument('--transpose',action='store',type=int)
args = parser.parse_args()
print(args.ceaser)
print(args.transpose)

if args.ceaser:
    cipher = Ceaser(args.ceaser)
    print(cipher.encrypt())
elif args.transpose:
    cipher = Transpose(args.transpose)
    print(cipher.encrypt())

# done = False

# try:
#     if sys.argv[1] == "--ceaser":
#         print(Ceaser().encrypt())
#         done = True
# except:
#     print("Usage 'python -m cryptozen --ceaser'")

# if done:
#     sys.exit()

# try:
#     if sys.argv[1] == "--file":
#         if os.path.exists(sys.argv[2]):
#             print(Files.Files().use_files(filename=sys.argv[2]))
#         else:
#             print("Filename wrong")
#         done = True
# except:
#     print("Usage 'python -m cryptozen --file filename.txt'")

# if done:
#     sys.exit()

# try:
#     if sys.argv[1] == "--transpose" and int(sys.argv[2]):
#         print(Transpose(key=int(sys.argv[2])).encrypt())
#     else:
#         print("Usage 'python -m cryptozen --transpose 12(any number)'")
#     done = True
# except:
#     print("Usage 'python -m cryptozen --transpose 12(any number)'")

# if done:
#     sys.exit()