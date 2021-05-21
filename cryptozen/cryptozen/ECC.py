import random
from RSAkeys import pre_prime_list
from Euclid import GCD
# from Recv_ECC import send_Data

p = pre_prime_list[46]

while True:
    a = random.randint(-p, p)
    b = random.randint(-p, p)
    if (4*pow(a,3) - 27*pow(b,2)) % p !=0:
        break

def point_doubling(q):
    return ((3*q[0]*q[0] + a)*GCD(2*q[1],p).extended_gcd()) % p

def do_add(ped, qed):
    if ped == qed:
        slope = point_doubling(ped)
    else:
        m = (ped[0] - qed[0]) % p
        slope = (ped[1] - qed[1])*GCD(m, p).extended_gcd()
    ans = [0, 0]
    ans[0] = (slope*slope - ped[0] - qed[0]) % p
    ans[1] = (slope*(ped[0] - ans[0]) - ped[1]) % p
    return ans

vals = []
def choose_points():
    for i in range(2):
        while True:
            x = random.randint(2, p)
            y = random.randint(2, p)
            if (pow(x,3) + a*x + b - y*y) % p == 0:
                break
        vals.append((x,y))
    return vals

def send_key():
    vals = choose_points()
    one = vals[0]
    select = one
    d = 4
    for i in range(d - 1):
        select = do_add(select, select)
    key = ((a,b,p),one,select)
    return key

# if __name__ == '__main__':
#     recv = send_Data()
#     print(recv)

