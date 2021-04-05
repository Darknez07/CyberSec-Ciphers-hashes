import unittest
from cryptozen.Transposition import Transpose


class Test(unittest.TestCase):
    def test_encrypt(self):
        obj = Transpose(21)
        x = obj.key
        ans = obj.encrypt("Hello boys encryption")
        self.assertIsInstance(ans, str)
        self.assertNotEqual(x, obj.key)

    def test_encrypt_mod_key(self):
        obj = Transpose(210)
        x = obj.key
        wo = "Hello boys welcome to encryption"
        val = obj.encrypt(wo)
        self.assertEqual(x % len(wo), obj.key)
        self.assertIsNotNone(obj.key)

    def test_encrypt_equal_length(self):
        obj = Transpose(25)
        k = obj.key
        val = obj.encrypt("Hello from the encryption")
        nk = obj.key
        self.assertNotEqual(k, nk)

    def check_empty_decenc(self):
        obj = Transpose(123)
        with self.assertRaises(Exception):
            obj.encrypt("")
        with self.assertRaises(Exception):
            obj.decrypt("")

    def test_encrypt(self):
        obj = Transpose(12)
        orig = "Code this in most logical way"
        val = obj.encrypt(orig)
        val2 = obj.decrypt(val)
        self.assertEqual(orig, val2)

    def test_decrypt(self):
        obj = Transpose(12)
        orig = "Code with reason and logic"
        val = obj.encrypt(orig)
        self.assertIsInstance(val, str)


if __name__ == "__main__":
    unittest.main()
