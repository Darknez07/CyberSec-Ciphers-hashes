import math


class Transpose:
    def __init__(self, key):
        self.key = key
        self.encoded =""
        self.decoded = ""


    def encrypt(self, message):
        for i in range(self.key):
            self.encoded+=message[i::self.key]
        return self.encoded


    def decrypt(self, coded):
        times = math.ceil(len(coded)/self.key)
        kill = times*self.key - len(coded)
        plain = ['']*times
        col = 0
        row = 0
        for sym in coded:
            plain[col]+=sym
            col+=1
            if (col == times) or (col == times - 1 and row >= self.key - kill):
                col = 0
                row+=1
        self.decoded = ''.join(plain)
        return self.decoded
