import random
import unittest


from my.awesome.lib import MyAwesomeClass

class LibTest(unittest.TestCase):
    def test_random(self):
        random.seed(93)
        self.assertEqual(15664109486095685021, MyAwesomeClass.random_value())

    def test_really_random(self):
        c = MyAwesomeClass
        random.seed(42)
        self.assertEqual(1, c.random_digit())
        self.assertEqual(0, c.random_digit())
        self.assertEqual(4, c.random_digit())

if __name__ == '__main__':
    unittest.main()

