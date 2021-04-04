from cryptozen.Affine import symbols, Affine
import cryptozen.English as E
from cryptozen.Euclid import GCD


class HackAffine:
    def __init__(self,threshold=0.03,word_ratio=0.5):
        self.key = 0
        self.decoded = ""
        self.threshold = threshold
        self.word_ratio = word_ratio

    def crack(self, encrypted):
        for j in range(1,len(symbols)**2):
                f = Affine(j)
                f.extract_key()
                if GCD(f.keyA, len(symbols)).gcd() !=1:
                    continue
                decoded = f.decrypt(encrypted)
                english = E.English().check_words([decoded])
                if english[0] > self.threshold and english[1] > self.word_ratio:
                    print(decoded, "-->", english[0], ", ", english[1])
