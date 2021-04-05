from cryptozen.English import English as E
# from distribution import Plots
letters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`" \
          "abcdefghijklmnopqrstuvwxyz{|}~"
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


# .find(a letter) will give the position of the letter in the
# string making it easier to identify the decryption
# and encryption
# When u add more letters but then your code barely works
class Ceaser:
    def __init__(self, k = 5):
        if k == 0 or k is None:
            k = 5
        self.k = k
        self.encoded = ""
        self.encoded_simple = ""


    def encrypt(self,text = None):
        if text is None:
            your_str = input('Enter to encrpyt: ')
        else:
            your_str = text

        self.k%=len(letters)
        if self.k == 0:
            self.k = 7

        if your_str == "":
            raise Exception("None value cannot be encrypted")
        for i in your_str:
            self.encoded += letters[(letters.find(i) + self.k) % len(letters)]
        return self.encoded

    def encrypt_simple(self,text = None):
        if text is None:
            your_str = input('Enter to encrypt: ')
        else:
            your_str = text

        self.k%=len(letter)
        if self.k == 0:
            self.k = 6

        if your_str == "":
            raise Exception("None value cannot be encrypted")
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
            s = s.replace("Z", " ")
            eng = E().check_words([s.lower().capitalize()])
            if eng[0] > maxs:
                maxs = eng[0]
                ans = s.lower().capitalize()
        return ans
