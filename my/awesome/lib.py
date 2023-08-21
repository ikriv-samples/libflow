import random

class MyAwesomeClass:
    @staticmethod
    def random_value():
        return 3 # chosen by a dice roll, guaranteed to be random

    @staticmethod
    def random_digit():
        return random.randint(0, 9)
        
