import unittest
from cryptozen.Cracking_transposition import Hack_transposition
from cryptozen.Transposition import Transpose as T
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
        # print(arr)
        self.assertNotEqual(len(arr), 0)
        self.assertIsInstance(arr, dict)

if __name__ == '__main__':
    unittest.main()