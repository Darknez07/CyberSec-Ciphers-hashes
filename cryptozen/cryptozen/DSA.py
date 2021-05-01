from RSAkeys import get_primes
from Euclid import GCD
import math
import random
import os
# Step-1:-- GET PRIMES
p, q = get_primes()

# Step-2:-- GET N
n = p * q

# Step-3:-- GET Phi
phi = (p - 1) * (q - 1)

# Step 4:-- GET Public key
rn = random.randint(2**123, 2**256)
for e in range(rn, phi):
    if math.gcd(e, phi) == 1:
        break

# Step 5:-- GET Private key
d = GCD(e, phi).extended_gcd()

f = open('privatekey_for_dsa.txt','w+')
f.writelines([str(d)])
f.close()
f = open('nval_dsa.txt','w+')
f.writelines([str(n)])
f.close()
f = open('public_key_for_dsa.txt','w+')
f.writelines([str(e)])
f.close()

def sign(message, private, n):
    processed_message = list(map(ord, list(message)))
    encoded_message = []
    for x in processed_message:
        encoded_message.append(pow(x, private, n))
    ans = []
    for word in encoded_message:
        ans.append(str(hex(word)))
    of = open('DSA_encrypted.txt','w+')
    for word in ans:
        of.writelines([word])
        of.writelines('\n')
    of.close()
    print("Files saved as DSA_encrypted.txt")
    print()
    return ans

def store_xor():
    f = open('DSA_encrypted.txt','r')
    i = 0
    message = f.read().split('\n')
    for a in message:
        if i == len(message) - 1:
            break
        if i == 0:
            fzor = int(a, 16)
        else:
            fzor^=int(a, 16)
        i+=1
    f = open('DSA_value_of_file.txt','w+')
    f.writelines(hex(fzor))
    f.close()
    print("Final File hash saved as DSA_value_of_file.txt")
    print()

# do_SHA(message)
file = input('Enter the filename with extension: ')
if os.path.exists(file):
    f = open(file,'r')
else:
    raise Exception("File Does not exists")
privat = open('privatekey_for_dsa.txt','r')
priv = int(privat.read())
privat.close()
pub = open('nval_dsa.txt','r')
ned = int(pub.read())
pub.close()
sign(f.read(), priv, ned)
f.close()
store_xor()
