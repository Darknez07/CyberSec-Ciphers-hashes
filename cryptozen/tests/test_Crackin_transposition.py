import unittest
from cryptozen.Cracking_transposition import Hack_transposition
from cryptozen.Transposition import Transpose as T
import os

class Test(unittest.TestCase):

    def test_first_input(self):
        obj = Hack_transposition()
        with self.assertRaises(Exception):
            obj.possible_ans("")

    def test_second_input(self):
        obj = Hack_transposition()
        with self.assertRaises(Exception):
            obj.possible_ans(None)

    def test_output_correction(self):
        sts = "Code with test cases to be on the safe side"
        obj = T(12)
        ans = obj.encrypt(sts)
        obj2 = Hack_transposition()
        arr = obj2.hack_transposition(ans)
        self.assertNotEqual(len(arr), 0)
        self.assertIsInstance(arr, dict)

    def test_output_correction_keys(self):
        sts = "Code with test cases to be on the safe side"
        obj = T(12)
        ans = obj.encrypt(sts)
        obj2 = Hack_transposition()
        arr = obj2.hack_transposition(ans)
        ek = list(arr.keys())[0]
        self.assertIsInstance(ek, tuple)
        self.assertIsInstance(ek[0], float)
        self.assertIsInstance(ek[1], float)

    def test_output_correction_vals(self):
        sts = "Code with test cases to be on the safe side"
        obj = T(12)
        ans = obj.encrypt(sts)
        obj2 = Hack_transposition()
        arr = obj2.hack_transposition(ans)
        ek = list(arr.values())[0]
        self.assertIsInstance(ek,list)
        self.assertIsInstance(ek[0],str)
        self.assertIsInstance(ek[1],int)

    def test_final_output(self):
        sts = "Code with test cases to be on the safe side"
        obj = T(12)
        ans = obj.encrypt(sts)
        obj2 = Hack_transposition()
        arr = obj2.hack_transposition(ans)
        check = sorted(arr.items(), key=lambda x: x[0])
        maxed = 0.0
        key = 0
        for i in check:
            if i[0][0] > maxed:
                maxed = i[0][0]
                key = i[1][-1]
                if key == 12:
                    break
        self.assertEqual(key,12)
        self.assertNotEqual(maxed, 0.0)

    def test_for_output_files(self):
        sts = "Code with test cases to be on the safe side"
        obj = T(12)
        ans = obj.encrypt(sts)
        obj2 = Hack_transposition()
        obj2.possible_ans(ans)
        lst = []
        for file in obj2.fnames:
            try:
                lst.append(int(file.split(' ')[-1].split('.')[0]))
            except Exception:
                pass
            # Cleanup
            os.remove(file)
        if 12 not in lst:
            self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()