import unittest
import cryptozen.Affine as a


class Test(unittest.TestCase):
    def test_input(self):
        obj = a.Affine(2303)
        with self.assertRaises(Exception):
            obj.encrypt("")
        with self.assertRaises(Exception):
            obj.decrypt("")

    def test_big_num(self):
        with self.assertRaises(Exception):
            obj = a.Affine(2 ** 1231123111)
            obj.encrypt("124123512")

    def test_choose_new_key(self):
        obj = a.Affine(22)
        value = obj.choose_key()
        n = a.GCD(value // len(a.symbols), len(a.symbols)).extended_gcd()
        self.assertIsInstance(n, int)
        self.assertIsNotNone(n)

    def test_encrypt_affine(self):
        obj = a.Affine(2011)
        ans = obj.encrypt("Hello boys")
        self.assertIsInstance(ans, str)

    def test_check_key_exit(self):
        with self.assertRaises(SystemExit) as cm:
            obj = a.Affine(1).encrypt("Kuch bhi lelo")
        self.assertEqual(
            cm.exception.args[0],
            "keyA is  0 choose a different key")

        with self.assertRaises(SystemExit) as cm:
            obj = a.Affine(97).encrypt("Kuch bhi karlo")
        self.assertEqual(
            cm.exception.args[0], "KeyA is 1 which is a weak key and easily crackable"
        )

        with self.assertRaises(SystemExit) as cm:
            obj = a.Affine(2)
            obj.keyA = -2
            obj.check_key()
        self.assertEqual(
            cm.exception.args[0],
            "KeyB is less than 0 or keyA is less than 0, Please choose different key",
        )


if __name__ == "__main__":
    unittest.main()
