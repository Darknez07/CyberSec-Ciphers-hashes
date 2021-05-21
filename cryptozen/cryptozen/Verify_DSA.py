import os

file = input("Enter the filename with extension: ")
if os.path.exists(file):
    f = open(file, "r")
else:
    raise Exception("Please enter the correct filename")

q = open("DSA_value_of_file.txt", "r")
p = open("DSA_encrypted.txt", "r")
pub = open("public_key_for_dsa.txt", "r")
pkey = int(pub.read())
nv = open("nval_dsa.txt", "r")
n = int(nv.read())

nv.close()
pub.close()

vals = []
i = 0
for l in p.read().split("\n")[:-1]:
    val = int(l, 16)
    ans = pow(val, pkey, n)
    if i == 0:
        fzor = val
    else:
        fzor ^= val
    i += 1
    vals.append(ans)
p.close()

if int(q.read(), 16) != fzor:
    print("File was tampered")

for w, u in zip(vals, f.read()):
    if chr(w) != u:
        raise Exception("File was tampered with")
print("File verified successfully")