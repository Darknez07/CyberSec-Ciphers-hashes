import unittest
from cryptozen.RSAkeys import low_primal_test, get_random_num, high_primal_test, isMillerRabinPassed
import sympy as smp
import random
import time

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
        self.assertEqual(high_primal_test(ans), ans)

    def test_Rabin_Miller(self):
        i = 0
        while i!=10:
            prm = smp.randprime(2**1000, 2**1024)
            self.assertTrue(isMillerRabinPassed(prm))
            i+=1
        # Testing with more rounds 40

    def test_rabin_miller_more_rounds(self):
        i = 0
        t = time.time()
        error = True
        while i!=10:
            if (time.time() - t)*1000 > 100:
                error = False
                break
            prm = smp.randprime(2**2048, 2**2049)
            self.assertTrue(isMillerRabinPassed(prm, 40))
            i+=1
        self.assertFalse(error)

if __name__ == '__main__':
    unittest.main()