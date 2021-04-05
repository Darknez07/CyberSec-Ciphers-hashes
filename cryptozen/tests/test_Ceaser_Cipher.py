import unittest
import cryptozen.Ceaser_Cipher as Cs
from cryptozen.Ceaser_Cipher import letter, letters


class Test(unittest.TestCase):
    def test_encrypt_simple(self):
        obj = Cs.Ceaser(12)
        ans = obj.encrypt_simple("Code in simple terms")
        self.assertIsInstance(ans, str)

    def test_encrypt_simple_input(self):
        obj = Cs.Ceaser(12)
        ans = obj.encrypt_simple("Cry for years and die with a tumour in your heart")
        for i in ans:
            self.assertIn(i, letter)

    def test_key_len(self):
        obj = Cs.Ceaser(122)
        ans = obj.encrypt_simple("Code for simple words and explain complex things")
        self.assertNotEqual(obj.k, 122)
        self.assertTrue(0 < obj.k < len(letter))

    def test_zero_key(self):
        obj = Cs.Ceaser(len(letter))
        ans = obj.encrypt_simple("Kuch bhi ala bhala")
        self.assertNotEqual(obj.k, 0)

    def test_encrypt_complex_input(self):
        obj = Cs.Ceaser(14)
        ans = obj.encrypt("Code with caution and exploit test cases")
        for i in ans:
            self.assertIn(i, letters)

    def test_encrypt_simple_error(self):
        obj = Cs.Ceaser()
        with self.assertRaises(Exception):
            obj.encrypt_simple("")

    def test_decrypt_simple(self):
        obj = Cs.Ceaser(12)
        plain = "Code in simple terms"
        ans = obj.encrypt_simple(plain)
        res = obj.decrypt_simple(ans)
        self.assertEqual(res, plain)


if __name__ == "__main__":
    unittest.main()
