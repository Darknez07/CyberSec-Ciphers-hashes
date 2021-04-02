import random
import sys
from cryptozen.Euclid import GCD
# from cryptozen.distribution import Plots
import time

symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~"""


class Affine:
    def __init__(self, key=None):
        self.key = key
        self.encoded = ""
        self.decoded = ""
        self.keyA = 0
        self.keyB = 0
        self.inv = None
        self.t = time.time()

    def run(self):
        self.key = self.choose_key()
        self.check_key()

    def choose_key(self):
        if self.key and GCD(self.key, len(symbols)).gcd() == 1:
            self.extract_key()
            return self.key
        else:
            while True:
                keyA = random.randint(1, len(symbols))
                keyB = random.randint(1, len(symbols))
                if GCD(keyA, len(symbols)).gcd() == 1:
                    self.keyA = keyA
                    self.keyB = keyB
                    return keyA * len(symbols) + keyB

    def extract_key(self):
        self.keyA = self.key // len(symbols)
        self.keyB = self.key % len(symbols)

    def get_inv(self):
        self.inv = GCD(self.keyA, len(symbols)).extended_gcd()

    def check_key(self):
        if self.keyA == 1:
            sys.exit('KeyA is 1 which is a weak key and easily crackable')
        if self.keyA == 0:
            sys.exit('keyA is  0 choose a different key')
        if self.keyB < 0 or self.keyA < 0 or self.keyB > len(symbols) - 1:
            sys.exit('KeyB is less than 0 or keyA is less than 0, Please choose different key')

    def encrypt(self, message):
        if message is "":
            raise Exception("Enter a proper message to encrypt")
        self.run()
        for sym in message:
            if sym in symbols:
                index = symbols.find(sym)
                self.encoded += symbols[(index * self.keyA + self.keyB) % len(symbols)]
        return self.encoded

    def decrypt(self, message):
        # self.run()
        if message is "":
            raise Exception("Enter a proper message to decrypt")
        self.extract_key()
        self.get_inv()
        for sym in message:
            index = symbols.find(sym)
            if self.keyB and self.inv:
                self.decoded += symbols[(index - self.keyB) * self.inv % len(symbols)]
        return self.decoded
