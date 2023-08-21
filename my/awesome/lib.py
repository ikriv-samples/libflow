import random
from itertools import chain

def _crange(begin, end):
    for c in range(ord(begin), ord(end)+1):
        yield chr(c)

_random_string_chars = list(
    chain(_crange('a','z'), 
          _crange('A','Z'), 
          _crange('0', '9'),
          "!@#$%^&*_"))

class MyAwesomeClass:
    @staticmethod
    def random_value():
        """Returns random integer value up to 2**64"""
        return random.randint(0, 2**64-1)

    @staticmethod
    def random_digit(base = 10):
        """Returns random digit of given base"""
        return random.randint(0, base-1)

    @staticmethod
    def random_string(length):
        """Returns a random string of given length"""
        nchars = len(_random_string_chars)
        return ''.join( _random_string_chars[random.randint(0,nchars)] for n in range(0, length))
