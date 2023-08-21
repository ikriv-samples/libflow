import unittest
from my.awesome.lib import MyAwesomeClass

class LibTest(unittest.TestCase):
    def test_random(self):
        self.assertEqual(3, MyAwesomeClass().random_value())

if __name__ == '__main__':
    unittest.main()

