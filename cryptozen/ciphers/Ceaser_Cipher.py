s = " "
letters = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# .find(a letter) will give the position of the letter in the
# string making it easier to identify the decryption
# and encryption
# When u add more letters but then your code barely works

def encrpyt():
    global s
    your_str = input('Enter to encrpyt: ')
    k = int(input('Enter the shift of letters: '))
    for i in your_str:
        s += letters[(letters.find(i)+k) % len(letters)]
    return s


def decrypt(text):
    for j in range(len(letters)):
        s = " "
        for i in text:
            if i == letters.find(" "):
                s += " "
            else:
                s += letters[(letters.find(i) - j) % len(letters)]

        print(s)

def decryptsimple(text):
    s = ""
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for j in range(len(letter)):
        s = ""
        for i in text:
            if i.isalnum():
                s += letter[(letter.find(i) - j) % 26]
            else:
                s += i
        print(s.lower().capitalize())
#
# x = encrpyt()
# print(x)
decryptsimple("ZFBI. J'N QSFUUZ TVSF NZ DBU XPVME FBU NF")