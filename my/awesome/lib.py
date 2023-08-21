import random

class MyAwesomeClass:
    @staticmethod
    def random_value():
        """Returns random integer value up to 2**64"""
        return random.randint(0, 2**64-1)

    @staticmethod
    def random_digit(base = 10):
        """Returns random digit of given base"""
        return random.randint(0, base-1)
        
