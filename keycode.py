import math
import random


def odd_length(func):
    def wrapper(*args, **kwargs):
        p = func(*args, **kwargs)
        while len(str(p)) % 2 == 0:
            p = func(*args, **kwargs)
        return p
    return wrapper

def pair_length(func):
    def wrapper(*args, **kwargs):
        p = func(*args, **kwargs)
        while len(str(p)) % 2 == 1:
            p = func(*args, **kwargs)
        return p
    return wrapper

@pair_length
def generate_prime(bits: int) -> int:
    # This function generates a prime number
    search = True
    while search:
        is_prime = True
        p = random.getrandbits(bits)
        for i in range(2, int(math.sqrt(p)) + 1):
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
        return 0, 1, 0
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b != 0:
        q = a // b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        # Update a,b
        a, b = b, r
        # Update for next iteration
        u0, u1 = u1, u
        v0, v1 = v1, v
    return a, u0, v0


def coprime(n: int, bits: int) -> int:
    # This function return a random coprime number of n 
    search = True
    while search:
        m = random.getrandbits(bits)
        gcd = math.gcd(n, m)
        if gcd == 1:
            return m


def inverse_module(n: int, mod: int) -> int:
    gcd, m, _ = euclidean_algorithm(n, mod)
    if gcd != 1:
        return 0
    return m % mod


class KeyCode:

    def __init__(self, k1:int = None, k2:int = None, k3:int = None) -> None:
        self._k1 = k1
        self._k2 = k2
        self._k3 = k3
        if (self._k1 is None) | (self._k2 is None) | (self._k3 is None):
            self._first_time = True
        else:
            self._first_time = False
        
    def __bool__(self) -> bool:
        if (self._k1 is None) | (self._k2 is None) | (self._k3 is None):
            return False
        else:
            return True
        
    def __str__(self) -> str:
        data = f'k1={str(self._k1)}\nk2={str(self._k2)}\nk3={str(self._k3)}'
        return data
    
    def __call__(self):
        return self._generate_key()
    
    def _generate_key(self, bytes_k1: int = 50, bytes_k2: int = 55) -> None:
        
        if self._first_time:
            self._k1 = generate_prime(bytes_k1)
            self._k2 = coprime(self._k1 - 1, bytes_k2)
            self._k3 = inverse_module(self._k2, self._k1 - 1)
            self._first_time = False
        else:
            print('The KeyCode can generate keys only once')

