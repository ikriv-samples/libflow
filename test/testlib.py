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

    def test_random_string(self):
        random.seed(43)
        # TODO: this is probably not the best way to test random_string
        # We should monkey-patch random.rand_int(), so we have control over
        # actual output
        self.assertEqual("eK", MyAwesomeClass.random_string(2))
        self.assertEqual("s7Vm6@c$3V", MyAwesomeClass.random_string(10))

    def test_random_string_no_symbols(self):
        random.seed(43)
        # TODO: this is probably not the best way to test random_string
        # We should monkey-patch random.rand_int(), so we have control over
        # actual output
        self.assertEqual("cs", MyAwesomeClass.random_string(2, allow_symbols=False))
        self.assertEqual("SWj9DxQSYg", MyAwesomeClass.random_string(10, allow_symbols=False))


if __name__ == '__main__':
    unittest.main()

