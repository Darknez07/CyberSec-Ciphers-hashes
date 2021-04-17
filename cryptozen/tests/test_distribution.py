import unittest
from cryptozen.distribution import Plots
import numpy as np
class Test(unittest.TestCase):

    def test_empty_message(self):
        obj = Plots()
        with self.assertRaises(Exception):
            obj.draw("")

    def test_see_plot(self):
        obj =Plots()
        obj.draw("Hello plot this for a check")
        self.assertIsInstance(obj.distribution, list)

    def test_the_type(self):
        obj = Plots()
        obj.draw("This test is such a good one",types="Something")
        self.assertIsInstance(obj.type,str)
        self.assertEqual(obj.type,"bar")

    def test_generated_set(self):
        obj = Plots()
        cl = "This test is such a good one"
        obj.draw(cl)
        srt = sorted(cl)
        srt2 = obj.sets
        for s in srt2:
            if s not in srt:
                self.assertEqual(1, 0)

    def test_for_density_plot(self):
        obj = Plots()
        s = obj.draw("Something is fishy and cryptography is booming",types="density")
        self.assertEqual(s.shape[0], 400)
        self.assertIsInstance(s, type(np.array([1.343,143.34])))
        for i in s:
            if not (0<= i <= 19):
                self.assertEqual(1, 0)

if __name__ == '__main__':
    unittest.main()
