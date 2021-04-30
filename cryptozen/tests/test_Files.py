import unittest
from cryptozen.Files import Files
from cryptozen.Affine import Affine, symbols
import os


class Test(unittest.TestCase):
    def test_get_encoded_exception(self):
        obj = Files(silent=True)
        with self.assertRaises(Exception):
            obj.return_encoded_array(filename="Anythingnotpresent.txt")
        with self.assertRaises(Exception):
            obj.return_encoded_array()

    def test_files_exceptions(self):
        obj = Files(silent=True)
        with self.assertRaises(Exception):
            obj.use_files(key=11, filename="Notes.txt", action="Anything")

    def test_for_affine_files(self):
        obj = Files(silent=True, obj=Affine(9584))
        obj.use_files(key=9584, filename="Notes.txt")
        self.assertIsInstance(obj.obj, Affine)
        if not os.path.exists("Notes encrypted.txt"):
            self.assertEqual(0, 1)

    def test_x_decoded_exception(self):
        on = Affine(303)
        s = on.key
        f = Files(silent=True, obj=on)
        f.use_files(key=s, filename="Notes.txt")
        Files(silent=True, obj=on).use_files(
            key=s, filename="Notes encrypted.txt", action="decrypt"
        )
        if not os.path.exists("Notes decrypted.txt"):
            self.assertEqual(1, 0)

    def test_z_encrypted(self):
        f = open("Notes encrypted.txt")
        g = open("Notes.txt")
        obj = Affine(303)
        kb = obj.encrypt(g.read())
        gb = f.read()
        g.close()
        f.close()
        self.assertTrue(kb == gb)

    def test_finalized(self):
        f = open("Notes decrypted.txt")
        g = open("Notes.txt")
        txt1 = f.read()
        txt2 = g.read()
        counter = {i: 0 for i in symbols}
        for i in txt1:
            counter[i] += 1
        for j in txt2:
            counter[j] -= 1
        k = set()
        for j in counter.keys():
            if counter[j] != 0:
                if counter[j] < 0:
                    k.add(-counter[j])
                else:
                    k.add(counter[j])
        correct = len(txt1) - sum(list(k))
        correct /= len(txt1)
        correct *= 100
        f.close()
        g.close()
        self.assertTrue(correct <= 100.0)
        correct = round(correct, 2)
        chck = [90 + (i / 10) for i in range(1, 101)]
        self.assertTrue(correct in chck)

    def test_decrypted_check(self):
        x = open("Notes encrypted.txt")
        y = open("Notes decrypted.txt")
        obj = Affine(303)
        ans = obj.decrypt(x.read())
        x.close()
        txt2 = y.read()
        counter = {i: 0 for i in symbols}
        for i in ans:
            counter[i] += 1
        for j in txt2:
            counter[j] -= 1
        k = set()
        for j in counter.keys():
            if counter[j] != 0:
                if counter[j] < 0:
                    k.add(-counter[j])
                else:
                    k.add(counter[j])
        correct = len(txt2) - sum(list(k))
        correct /= len(txt2)
        correct *= 100
        y.close()
        self.assertTrue(correct <= 100.0)
        correct = round(correct, 2)
        chck = [90 + (i / 10) for i in range(1, 101)]
        self.assertTrue(correct in chck)


if __name__ == "__main__":
    unittest.main()
