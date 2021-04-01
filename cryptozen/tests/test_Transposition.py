import unittest
from cryptozen.Transposition import Transpose

class Test(unittest.TestCase):

    def test_encrypt(self):
        obj = Transpose(21)
        x = obj.key
        ans = obj.encrypt("Hello boys encryption")
        self.assertIsInstance(ans, str)
        self.assertNotEqual(x, obj.key)

    def test_encrypt_same_key(self):
        obj = Transpose(210)
        x = obj.key
        wo = "Hello boys welcome to encryption"
        val = obj.encrypt(wo)
        self.assertEqual(x % len(wo), obj.key)
        self.assertIsNotNone(obj.key)

if __name__ == "__main__":
    unittest.main()