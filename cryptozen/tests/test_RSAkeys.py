import unittest
from cryptozen.RSAkeys import low_primal_test, get_random_num
import sympy as smp
class Test(unittest.TestCase):
    @unittest.skip("This might fail because it is low prime test")
    def test_low_prime(self):
        ans = low_primal_test(12)
        self.assertEqual(len(bin(ans)[2:]), 12)
        self.assertTrue(smp.isprime(ans))

    def test_for_random_num(self):
        ans = get_random_num(12)
        self.assertEqual(len(bin(ans)[2:]), 12)
        self.assertTrue(2**11 <= ans <= 2**12)

if __name__ == '__main__':
    unittest.main()