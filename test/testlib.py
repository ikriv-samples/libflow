import random
import unittest


from my.awesome.lib import MyAwesomeClass

class LibTest(unittest.TestCase):
    def test_random(self):
        random.seed(93)
        self.assertEqual(15664109486095685021, MyAwesomeClass.random_value())

    def test_random_digit(self):
        c = MyAwesomeClass
        random.seed(42)
        self.assertEqual(1, c.random_digit())
        self.assertEqual(0, c.random_digit())
        self.assertEqual(4, c.random_digit())

    def test_random_decimal_digit(self):
        c = MyAwesomeClass
        random.seed(42)
        # same as random_digit()
        self.assertEqual(1, c.random_digit(10))
        self.assertEqual(0, c.random_digit(10))
        self.assertEqual(4, c.random_digit(10))

    def test_random_hex_digit(self):
        c = MyAwesomeClass
        random.seed(42)
        # same as random_digit()
        self.assertEqual(3, c.random_digit(16))
        self.assertEqual(0, c.random_digit(16))
        self.assertEqual(8, c.random_digit(16))


if __name__ == '__main__':
    unittest.main()

