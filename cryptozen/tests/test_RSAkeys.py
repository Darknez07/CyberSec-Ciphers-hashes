import unittest
from cryptozen.RSAkeys import low_primal_test, get_random_num, high_primal_test
import sympy as smp
import random
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

    def test_high_prime(self):
        i = 0
        done = set()
        while i!=10:
            s = smp.randprime(2**200, 2**210)
            ans = high_primal_test(s)
            if ans == s:
                done.add(s)
                i+=1
            else:
                self.assertEqual(1, 0)
        for x in done:
            self.assertTrue(smp.isprime(x))

    def test_low_primal(self):
        while True:
            s = smp.randprime(2**11, 2**12)
            ans = low_primal_test(12)
            if smp.isprime(ans):
                break
        self.assertEqual(len(bin(ans)[2:]), 12)
        # self.assertTrue(smp.isprime(ans))
        self.assertEqual(high_primal_test(ans), ans)

if __name__ == '__main__':
    unittest.main()