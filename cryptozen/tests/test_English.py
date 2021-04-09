import unittest
import platform
import cryptozen.English as E


class Test(unittest.TestCase):
    obj = E.English()

    def test_get_english_words_file_presence(self):
        with self.assertRaises(Exception):
            self.obj.get_from_files("asfklasjf.txt")

    def test_get_english_words_file_type(self):
        with self.assertRaises(Exception):
            self.obj.get_from_files("../cryptozen/Wrong.pdf")

    def test_get_english_words_output(self):
        ans = self.obj.get_from_files("../cryptozen/Notes.txt")
        self.assertIsInstance(ans, list)

    def test_english_words_loader(self):
        self.obj.get_english_words()
        self.assertEqual(len(self.obj.english_words), 45304)

    def test_check_letters_type_negative(self):
        # Negative
        with self.assertRaises(Exception):
            self.obj.check_letters("alkshfalfhskashfkal")

        with self.assertRaises(Exception):
            self.obj.check_letters([1, 123, 14, 42141])

        a,b = self.obj.check_letters(
                ["akajsgfdajka-----afsj", "afsjkgaskjf273ajkhdagkagsj"]
            )
        self.assertEqual(a, 0)
        self.assertEqual(b, 0)

    def test_check_words(self):
        eng = E.English()
        eng.words = []
        a, b = eng.check_words(["akajsgfdajka-----afsj", "afsjkgaskjf273ajkhdagkagsj"])
        self.assertEqual(a, 0)
        self.assertEqual(b, 0)

    def test_check_words_negative(self):
        l = [
            "A story has no beginning or end: arbitrarily one chooses that moment of experience from which to look back or from which to look ahead.",
            "With determination and dice, I am God.",
            "I had had a feeling of freedom because of the sudden change in my life. ...",
            "We possess art lest we perish of the truth.",
        ]
        result = self.obj.check_words(l)
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], float)

    def test_check_letters_type_positive(self):
        l = [
            "A story has no beginning or end: arbitrarily one chooses that moment of experience from which to look back or from which to look ahead.",
            "With determination and dice, I am God.",
            "I had had a feeling of freedom because of the sudden change in my life. ...",
            "We possess art lest we perish of the truth.",
        ]
        # Positive
        prob = self.obj.check_letters(l)
        self.assertIsInstance(prob, tuple)
        self.assertIsInstance(prob[0], float)
        self.assertIsInstance(self.obj.words[0], str)


if __name__ == "__main__":
    unittest.main()
