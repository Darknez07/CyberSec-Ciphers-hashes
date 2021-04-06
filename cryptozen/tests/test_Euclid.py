import math as m
import platform
import random
import unittest

import cryptozen.Euclid as E
# import cryptozen.RSAkeys as RSAkeys


class Test(unittest.TestCase):
    def test_gcd_lower_limit(self):
        obj = E.GCD(0, 1)
        self.assertIsInstance(obj.gcd(), int)
        self.assertEqual(obj.gcd(), 1)

    def test_gcd_zero_case(self):
        count = 0
        while True:
            k = random.randint(5, 2 ** 8)
            obj = E.GCD(0, k).gcd()
            self.assertEqual(obj, k)
            count += 1
            if count == 10:
                break

    def test_gcd_special_case(self):
        with self.assertRaises(Exception):
            E.GCD(0, 0).gcd()

    def test_gcd_higher_limit(self):
        with self.assertRaises(Exception):
            ans = E.GCD(2 ** 1321111, 2 ** 1043201).gcd()

    def test_gcd_higher_limit_2(self):
        ans = E.GCD(2 ** 111111, 2 ** 111231).gcd()
        self.assertIsInstance(ans, int)
        val = m.log2(ans).is_integer()
        self.assertTrue(val)

    def test_gcd_negative_values(self):
        ans = E.GCD(-13, -31).gcd()
        self.assertEqual(ans, -1)
        self.assertLess(ans, 0)
        ans2 = E.GCD(-13, 31).gcd()
        self.assertEqual(ans2, -1)
        self.assertLess(ans2, 0)
        ans3 = E.GCD(-23498092384, -32877347123).gcd()
        self.assertLess(ans3, 0)

    def test_gcd_floating_point(self):
        with self.assertRaises(Exception):
            ans2 = E.GCD(1.123124, 32412.423).gcd()

        with self.assertRaises(Exception):
            ans2 = E.GCD(1.123, 2.000).gcd()

        ans3 = E.GCD(6.000, 3.000).gcd()
        self.assertIsInstance(ans3, int)

        with self.assertRaises(Exception):
            ans4 = E.GCD(4.0000, 321.3112421).gcd()

    def test_extended_gcd_condition(self):
        obj = E.GCD(200, 2)
        self.assertIsNone(obj.extended_gcd())
        count = 0
        while True:
            k = random.randint(-(2 ** 16), 2 ** 16)
            obj = E.GCD(0, k).extended_gcd()
            self.assertIsNone(obj)
            count += 1
            if count == 10:
                break

    # def test_extended_gcd_primes(self):
    #     count = 0
    #     start = 8
    #     while count != 7:
    #         a, b = RSAkeys.get_primes(start)
    #         ans = E.GCD(a, b).extended_gcd()
    #         if ans is None:
    #             a, b = RSAkeys.get_primes(start)
    #             ans = E.GCD(a, b).extended_gcd()
    #         self.assertEqual(E.GCD(ans * a, b).gcd(), 1)
    #         count += 1
    #         start *= 2

    # def test_limit_extended_gcd(self):
    #     count = 0
    #     start = 8
    #     while count != 7:
    #         a, b = RSAkeys.get_primes(start)
    #         ans = E.GCD(a, b).extended_gcd()
    #         self.assertIsNotNone(ans)
    #         self.assertIsInstance(ans, int)
    #         count += 1
    #         start *= 2

    def test_composite_case_extended_gcd(self):
        count = 0
        while count != 7:
            a = random.randint(2 ** 4, 2 ** 20)
            b = a * random.randint(3, 2 ** 5)
            x = E.GCD(a, b).extended_gcd()
            self.assertIsNone(x)
            count += 1


if __name__ == "__main__":
    unittest.main()
