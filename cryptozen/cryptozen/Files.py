import sys
import os
import random
from cryptozen.Transposition import Transpose as t
from cryptozen.Affine import Affine

class Files:
    def __init__(self, silent=False, obj = None):
        print("\nStarted\n")
        self.silent = silent
        self.filename = None
        self.obj = obj

    def return_encoded_array(self, filename=None):
        if filename is None:
            raise Exception("Enter a File name")
        encode = []
        if os.path.exists(filename):
            f = open(filename)
            encode = f.read()
            f.close()
            return encode
        else:
            raise Exception("Please enter file path clearly")

    def use_files(self, key=None, b=False, filename=None, action="encrypt"):
        if filename is None:
            filename = input("Enter the filename: ")
        encode = self.return_encoded_array(filename)
        # print(encode)
        all_at_once = False
        if key is None:
            key = random.choice(range(1, len(encode)))
        if self.obj is None:
            self.obj = t(key)
            print("Using Transposition cipher by default")
        elif isinstance(self.obj, Affine):
            self.obj = Affine(key)
            all_at_once = True
        if not b:
            # action = input('Enter the action to perform encrypt/decrypt >')
            encoder = []
            decoder = []
            action = action.lower()
            if action == "encrypt":
                encoder.append(self.obj.encrypt(encode))
            elif action == "decrypt":
                decoder.append(self.obj.decrypt(encode))
        else:
            return encode

        breaks = os.path.basename(filename)
        breaks = breaks.split(".")
        if action == "encrypt":
            with open(breaks[0] + " encrypted." + breaks[1], "w+") as k:
                k.writelines(encoder)

            print("Your encrypted file is saved as " + breaks[0] + " encrypted")
        elif action == "decrypt":
            f = breaks[0].split(" ")
            with open(f[0] + " decrypted." + breaks[1], "w+") as k:
                k.writelines(decoder)

            print("Your decrypted file is saved as " + f[0] + " decrypted")
        else:
            raise Exception("Re run and try again for action:-->")
            # sys.exit(1)
