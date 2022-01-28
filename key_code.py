import math
from random import random

def odd_length(func):
    pass

def generate_prime(bits):

    search = True
    while search:
        is_prime = True
        p = random.getrandbits(bits)
        for i in range(2, int(math.sqrt(p))+1 ):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            return p



class Key_code:

    def __init__(self) -> None:
        pass