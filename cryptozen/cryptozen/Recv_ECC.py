from ECC import send_key, do_add

key = send_key()

def get_data():
    num = 20
    return num

def find_P_on_curve(P):
    for i in range(2, key[0][2]):
        if (pow(P[0],3) + key[0][0]*P[0] + key[0][1] - i*i) % key[0][2] == 0:
            break
    P.append(i)
    return P

def  get_C1_C2(P, r, key):
    for i in range(r - 1):
        if i == 0:
            C1 = do_add(key[1], key[1])
        else:
            C1 = do_add(C1, C1)
    for i in range(r - 1):
        if i == 0:
            C2 = do_add(key[2], key[2])
        else:
            C2 = do_add(C2, C2)
    C2 = do_add(P,C2)
    return C1, C2

def send_Data():
    r = 4
    P = [get_data()]
    P = find_P_on_curve(P)
    print(P)
    C1, C2 = get_C1_C2(P,r,key)
    recv = (C1,C2,r)
    return recv

if __name__ == "__main__":
    print(send_Data())