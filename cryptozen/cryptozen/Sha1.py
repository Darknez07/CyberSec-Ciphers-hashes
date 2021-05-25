import random
import sys


def get_512_bits(message, conv=False):
    string = ""
    if conv == False:
        for j in message:
            string += bin(ord(j))[2:]
    ans = len(string)
    while len(string) != 448:
        string += "0"
    add = bin(ans)[2:]
    mod = ""
    while len(mod) != (64 - len(add)):
        mod += "0"
    mod += add
    string += mod
    return string


def distribute(string):
    words = []
    for i in range(16):
        words.append(int(string[i * 32 : (i + 1) * 32], 2))
    return words


def do_SHA(message=None, types="string"):
    H = []
    random.seed(0)
    while len(H) != 5:
        rnd = random.randint(3, 2 ** 9)
        H.append(rnd)
    show_res = False
    if message is None:
        message = input("Enter the message to encrypt: ")
        show_res = True
    keys = [1518500249, 1859775393, 2400959708, 3395469782]
    i = 0
    if types == "string":
        string = get_512_bits(message)
    elif types == "binary":
        string = get_512_bits(message, conv=True)
    print(string)
    words = distribute(string)
    for i in range(80):
        A = H[0]
        B = H[1]
        C = H[2]
        D = H[3]
        E = H[4]
        x = len(bin(H[0])[2:])
        y = len(bin(H[1])[2:])
        for i in range(len(H)):
            if len(bin(H[i])[2:]) > 160:
                H[i] = int(bin(H[i])[2:][:160], 2)
        if x < 32:
            x = 32
        if y < 32:
            y = 32
        if x > 160:
            x = 160
        if y > 160:
            y = 160
        if 79 >= i >= 16:
            words.append(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16])
            if len(bin(words[-1])[2:]) > 160:
                words[-1] = int(bin(words[-1])[2:][:160], 2)
        if 19 >= i >= 0:
            ans = B & C | ((~B) & D)
        if 39 >= i >= 20:
            ans = B ^ C ^ D
            i = 1
        if 59 >= i >= 40:
            ans = B & C | B & D | C & D
            i = 2
        else:
            ans = B ^ C ^ D
            i = 3
        if len(bin(ans)[2:]) > 160:
            ans = int(bin(ans)[2:][:160], 2)
        shift = A << 5 | A >> (x - 5)
        if len(bin(shift)[2:]) > 160:
            num = int(bin(shift)[2:][:160], 2)
        num = ans + shift + keys[i] + E + words[i]
        if len(bin(num)[2:]) > 160:
            num = int(bin(num)[2:][:160], 2)
        E = D
        D = C
        C = B << 30 | B >> (y - 30)
        B = A
        A = num
        H[0] += A
        H[1] += B
        H[2] += C
        H[3] += D
        H[4] += E

    H[0] = H[0] << 128 | H[0] >> (160 - 128)
    H[1] = H[1] << 96 | H[1] >> (160 - 96)
    H[2] = H[2] << 64 | H[2] >> (160 - 64)
    H[3] = H[3] << 32 | H[3] >> (160 - 32)
    result = H[0] | H[1] | H[2] | H[3] | H[4]
    if len(bin(result)[2:]) > 160:
        result = int(bin(result)[2:][:160], 2)
    if show_res:
        print(hex(result))
    return result, string


if __name__ == '__main__':
    result, string = do_SHA()
    print("Now we do the HMAC")
    # Choose a key
    key = input("Enter the key: ")
    keyed = ""
    ipad = int("0x" + "36" * 64, 16)
    opad = int("0x" + "5C" * 64, 16)
    for j in key:
        keyed += bin(ord(j))[2:]
    # Step 1 append the '0's
    while len(keyed) != 512:
        keyed += "0"
    # Step 2 get the new string with xor
    new_string = bin(int(keyed, 2) ^ ipad)[2:]
    # Step 3 apply Sha to new_string
    result2, new_string = do_SHA(new_string, types="binary")
    close = bin(result2)[2:] + string
    # Step 4 xor from the key to opad and result to the new_string obtained
    new_string_2 = bin(int(keyed, 2) ^ opad)[2:]
    result3, new_string_2 = do_SHA(new_string_2, types="binary")
    ans = close + new_string_2
    res = ""
    # Step 5 apply the SHA finally to attain 1536 bits of result/
    for i in range(2):
        res += bin(do_SHA(ans[i * 512 : (i + 1) * 512], types="binary")[0])[2:]
    # Last 160 bits of result
    res += bin(do_SHA(ans[1024:], types="binary")[0])[2:]
    print(hex(int(res, 2)))
