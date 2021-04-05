from cryptozen.Euclid import GCD
import random


class Transpose:
    def __init__(self, key):
        self.key = key
        self.encoded = ""
        self.decoded = ""

    def encrypt(self, message=None):
        if message is None:
            message = input("Enter message to encrypt: ")
        if self.key == len(message):
            while True:
                x = random.randint(3, len(message))
                if GCD(len(message), x).gcd() == 1:
                    self.key = x
                    break
        else:
            self.key = self.key % len(message)
        for i in range(self.key):
            self.encoded += message[i :: self.key]
        return self.encoded

    def decrypt(self, coded):
        if len(coded) % self.key == 0:
            times = len(coded) // self.key
        else:
            times = (len(coded) // self.key) + 1

        kill = times * self.key - len(coded)
        plain = [""] * times
        col = 0
        row = 0
        for sym in coded:
            plain[col] += sym
            col += 1
            if (col == times) or (col == times - 1 and row >= self.key - kill):
                col = 0
                row += 1
        self.decoded = "".join(plain)
        return self.decoded
