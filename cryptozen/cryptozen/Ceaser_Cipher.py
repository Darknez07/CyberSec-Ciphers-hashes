from cryptozen.English import English as E
# from distribution import Plots
letters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`" \
          "abcdefghijklmnopqrstuvwxyz{|}~"
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# .find(a letter) will give the position of the letter in the
# string making it easier to identify the decryption
# and encryption
# When u add more letters but then your code barely works
class Simple:
    def __init__(self, k = 5):
        self.k = k
        self.encoded = ""
        self.encoded_simple = ""

    def encrpyt(self,text = None):
        if text is None:
            your_str = input('Enter to encrpyt: ')
        else:
            your_str = text
        for i in your_str:
            self.encoded += letters[(letters.find(i) + self.k) % len(letters)]
        return self.encoded

    def encrypt_simple(self,text = None):
        if text is None:
            your_str = input('Enter to encrypt: ')
        else:
            your_str = text
        for i in your_str:
            self.encoded_simple += letter[(letter.find(i) + self.k) % len(letter)]
        return self.encoded_simple

    def decrypt(self,text):
        ans = " "
        maxs = 0
        for j in range(len(letters)):
            s = ""
            for i in text:
                s += letters[(letters.find(i) - j) % len(letters)]
            # print(s)
            eng = E().check_words([s])
            if eng[0] > maxs:
                maxs = eng[0]
                ans = s
        return ans

    def decrypt_simple(self,text):
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
        return ans
