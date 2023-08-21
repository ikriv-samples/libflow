import random

class MyAwesomeClass:
    def random_value(self):
        """Returns random integer value up to 2**64"""
        return random.randint(0, 2**64-1)

    def random_digit(self):
        """Returns random decimal digit"""
        return random.randint(0, 9)
        
