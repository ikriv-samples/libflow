import random
from itertools import chain

def _crange(begin, end):
    for c in range(ord(begin), ord(end)+1):
        yield chr(c)

_alphanumeric = list(
    chain(_crange('a','z'), 
          _crange('A','Z'), 
          _crange('0', '9')))

_symbols = "!@#$%^&*_"

_alphanumeric_and_symbols = list(chain(_alphanumeric, _symbols))

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
    def random_string(length, *, allow_symbols = True):
        """Returns a random string of given length"""
        charset = _alphanumeric_and_symbols if allow_symbols else _alphanumeric
        nchars = len(charset)
        return ''.join(charset[random.randint(0,nchars)] for n in range(0, length))
