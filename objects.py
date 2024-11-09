import random
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Optional, Tuple
from math import sqrt, gcd


@dataclass
class Key:
    k1: int
    k2: int
    k3: int


@dataclass
class Message:
    message: list[str]


@dataclass
class GenerateNumber:
    k: int
    seed: Optional[int] = None

    def __post_init__(self):
        if not isinstance(self.k, int) or self.k <= 0:
            raise ValueError("k should be a int positive.")

    def generate(self) -> int:
        if self.seed is not None:
            random.seed(self.seed)
        num = random.choices("1234567890", k=self.k)
        # Asegurar que el primer dígito no sea cero
        while num[0] == '0':
            num = random.choices("1234567890", k=self.k)
        num = "".join(num)
        return int(num)


@dataclass
class GeneratePrime:
    generate_number: GenerateNumber

    def generate(self) -> int:
        while True:
            p = self.generate_number.generate()
            if self.is_prime(p):
                return p

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


@dataclass
class GenerateKey:
    generate_prime: GeneratePrime
    generate_number: GenerateNumber

    def euclidean_alg(self, a: int, b: int) -> Tuple[int, int, int]:
        """gcd = Greatest Common Divisor
            gcd = a*n + b*m

        Args:
            a (int): int >= 0
            b (int): int >= 0

        Returns:
            Tuple[int, int, int]: gcd, n, m
        """
        if b == 0:
            return a, 1, 0

        u0, u1 = 1, 0
        v0, v1 = 0, 1
        while b != 0:
            q = a // b
            r = a % b
            u = u0 - q * u1
            v = v0 - q * v1
            # Update
            a, b = b, r
            # Update for next iter
            u0, u1 = u1, u
            v0, v1 = v1, v

        return a, u0, v0

    def find_coprime(self, m: int) -> int:
        while True:
            n = self.generate_number.generate()
            if self.is_coprime(n, m):
                return n

    def is_coprime(self, n: int, m: int) -> bool:
        g = gcd(m, n)
        if g == 1:
            return True
        return False

    def inverse_module(self, n: int, mod: int) -> int:
        g, m, _ = self.euclidean_alg(n, mod)
        if g != 1:
            return 0
        return m % mod

    def generate(self) -> Key:
        p = self.generate_prime.generate()
        e = self.find_coprime(p - 1)
        d = self.inverse_module(e, p - 1)
        return Key(k1=p, k2=e, k3=d)


@dataclass
class StrToInt:
    message = Message

    def convert(self): ...


@dataclass
class Encryp:
    key: Key

    def encryp(self, message: Message) -> Message: ...


@dataclass
class Decryp:
    key: Key

    def decryp(self, message: Message) -> Message: ...


if __name__ == "__main__":
    try:
        generate_prime = GeneratePrime(GenerateNumber(15))
        generate_number = GenerateNumber(12)
        generate_key = GenerateKey(
            generate_prime=generate_prime, generate_number=generate_number)
        key = generate_key.generate()
        print(f"{key.k1=}")
        print(f"{key.k2=}")
        print(f"{key.k3=}")
        input("Finished")

    except:
        input("ERROR")
