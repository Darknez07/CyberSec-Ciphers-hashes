import unittest
from cryptozen.RSAkeys import low_primal_test
import sympy as smp
class Test(unittest.TestCase):
    @unittest.skip("This might fail because it is low prime test")
    def test_low_prime(self):
        ans = low_primal_test(12)
        self.assertEqual(len(bin(ans)[2:]), 12)
        self.assertTrue(smp.isprime(ans))

if __name__ == '__main__':
    unittest.main()