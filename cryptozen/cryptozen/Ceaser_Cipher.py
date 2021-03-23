from English import English as E
s = ""
letters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`" \
          "abcdefghijklmnopqrstuvwxyz{|}~"
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# .find(a letter) will give the position of the letter in the
# string making it easier to identify the decryption
# and encryption
# When u add more letters but then your code barely works

def encrpyt(text = None, k = 5):
    global s
    if text is None:
        your_str = input('Enter to encrpyt: ')
        k = int(input('Enter the shift of letters: '))
    else:
        your_str = text
    for i in your_str:
        s += letters[(letters.find(i) + k) % len(letters)]
    return s


def decrypt(text):
    ans = " "
    maxs = 0
    for j in range(len(letters)):
        s = ""
        for i in text:
            s += letters[(letters.find(i) - j) % len(letters)]
        eng = E().check_words([s])
        print(s,eng)
        if eng[0] > maxs:
            maxs = eng[0]
            ans = s
    print(ans)


def decrypt_simple(text):
    maxs = 0
    ans = ""
    for j in range(len(letter)):
        s = ""
        for i in text:
            if i.isalnum():
                s += letter[(letter.find(i) - j) % 26]
            else:
                s += i
        eng = E().check_words([s.lower().capitalize()])
        print(s.lower().capitalize())
        if eng[0] > maxs:
            maxs = eng[0]
            ans = s.lower().capitalize()
    print(ans)



