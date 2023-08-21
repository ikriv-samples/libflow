import random

class MyAwesomeClass:
    @staticmethod
    def random_value():
        """Returns random integer value up to 2**64"""
        return random.randint(0, 2**64-1)

    @staticmethod
    def random_digit():
        """Returns random decimal digit"""
        return random.randint(0, 9)

    @staticmethod
    def random_string(length):
        """Returns a random string of given length"""
        raise NotImplementedError()
        
