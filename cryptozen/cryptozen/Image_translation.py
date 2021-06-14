import numpy as np
from cryptozen.RSAkeys import get_primes
from cryptozen.Euclid import GCD
import random
import matplotlib.pyplot as plt


class Scaling:
    def __init__(self,inv=False):
        self.inv = inv
        self.max = 0.0
        self.min = 0.0
        self.called_fit = False

    def fit_transform(self,data,target_max=1,target_min=0):
        self.max = data.max()
        self.min = data.min()
        self.called_fit = True
        data = (data - self.min) / (self.max - self.min)
        data*=(target_max - target_min)
        data+=target_min
        return data

    def inverse_transform(self,data):
        if not self.called_fit:
            raise Exception("Call fit")
        else:
            mins = data.min()
            maxs = data.max()
            data = (data - mins) / (maxs - mins)
            data*=(self.max - self.min)
            data+=self.min
            return data

def get_rsa_vals():
    # Step-1:-- GET PRIMES
    p, q = get_primes(64)

    # Step-2:-- GET N
    n = p * q

    # Step-3:-- GET Phi
    phi = (p - 1) * (q - 1)

    # Step 4:-- GET Public key
    for e in range(3, phi):
        if GCD(e, phi).gcd() == 1:
            break

    # Step 5:-- GET Private key
    d = GCD(e, phi).extended_gcd()
    return d,e,n

d,e,n = get_rsa_vals()

def encrypt(x):
    return pow(int(x), e, n)

def decrypt(x):
    return pow(int(x), d, n)

if __name__ == '__main__':
    vf = np.vectorize(encrypt)
    vfd = np.vectorize(decrypt)
    arr = plt.imread("Bhole.jpg")
    plt.imshow(arr)
    plt.show()
    arr_new = arr.T

    new_ar = []
    obj_arr = []
    for ar in arr_new:
        ar = ar.astype(np.int64)
        ak = vf(ar)
        new_ar.append(ak)

    arrn = new_ar
    new_ar = np.array(new_ar).T

    std = Scaling()
    vals = std.fit_transform(new_ar,target_max=190.0,target_min=0.0)
    plt.imshow(vals)
    plt.show()

    new_ar = arrn
    j = 0
    arrs = []
    for ar in new_ar:
        ar = ar.astype(np.int64)
        ak = vfd(ar)
        arrs.append(ak)
        j+=1

    arrs = np.array(arrs)
    plt.imshow(arrs.T)
    plt.show()