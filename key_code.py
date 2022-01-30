import math
import random

def odd_length(func):
    def wrapper(*args, **kwargs):
        p = func(*args, **kwargs)
        while len(str(p)) % 2 == 0:
            p = func(*args, **kwargs)
        return p
    return wrapper

@odd_length
def generate_prime(bits: int) -> int: 
    # This function generates a prime number
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

def euclidean_algorithm(a: int, b: int) -> tuple:
    # output: gcd , n , m 
    # where gcd = a*n + b*m
    # gcd = Greatest Common Divisor
    if b == 0:
        return 0,1,0
    u0 , u1 = 1 , 0
    v0 , v1 = 0 , 1
    while b != 0:
        q = a//b
        r = a - b*q
        u = u0 - q*u1
        v = v0 - q*v1
        # Update a,b
        a , b = b , r
        # Update for next iteration
        u0 , u1 = u1 , u
        v0 , v1 = v1 , v
    return a , u0 , v0

def coprime(n: int, bits: int) -> int:
    # This function return a random coprime number of n 
    search = True
    while search:
        m = random.getrandbits(bits)
        gcd = math.gcd(n,m)
        if gcd == 1:
            search = False
            return m

def inverse_module(n: int, mod: int) -> int:
    gcd, m , _ = euclidean_algorithm(n, mod) 
    if gcd != 1:
        return 0
    return m % mod

class Key_code:

    def __init__(self) -> None:
        self.p = int
        self.e = int
        self.d = int

    def generate_key(self, bytes_p: int = 40, bytes_e: int = 30) -> None:
        self.p = generate_prime(bytes_p)
        self.e = coprime(self.p - 1, bytes_e)
        self.d = inverse_module(self.e, self.p - 1)
