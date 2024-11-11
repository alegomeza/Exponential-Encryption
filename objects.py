import random
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Optional, Tuple, List
from math import sqrt, gcd


@dataclass
class PowerMod:
    exp: int
    mod: int

    def power(self, num: int) -> int:
        bin_exp = bin(self.exp)
        bin_exp = bin_exp[2:]
        max_power = len(bin_exp)
        
        pow_tow = self.power_tower(num=num, max_power=max_power)
        
        result = 1
        for idx in range(max_power):
            if bin_exp[idx] == "1":
                result *= pow_tow[idx]
                result %= self.mod
        
        return result

    def power_tower(self, num: int, max_power: int) -> List[int]:
        pow_tow = [num % self.mod]
        for _ in range(1, max_power):
            power = pow_tow[0] ** 2 % self.mod
            pow_tow.insert(0, power)
        return pow_tow


@dataclass
class Letters:
    """
    Letters that be used for make messages

    Attributes:
    KEYS: str -- letters without repetition 

    Methods:
    to_int() --
    to_str() --
    """
    KEYS: str

    def __post_init__(self):
        if len(self.KEYS) != len(set(self.KEYS)):
            raise ValueError("The are characters that repeat themselves")

    def range(self):
        return len(self.KEYS)

    def to_int(self, value: str) -> int:
        dict_prov = {self.KEYS[idx]: int(idx) for idx in range(self.range())}
        return dict_prov[value]

    def to_str(self, value: int) -> str:
        dict_prov = {int(idx): self.KEYS[idx] for idx in range(self.range())}
        return dict_prov[value]


@dataclass
class Key:
    k1: int
    k2: int
    k3: int

    def convert(self, num: int, mode:str = "encrypt"):
        mod = self.k1
        if mode == "encrypt":
            exp = self.k2
        elif mode == "decrypt":
            exp = self.k3
        else:
            raise ValueError(f"{mode} is not a mode.\nmode: \"encrypt\" | \"decrypt\"" )
        power_mod = PowerMod(exp=exp, mod=mod)
        return power_mod.power(num=num)


@dataclass
class Message:
    message: List[str]

    def __str__(self):
        return "\n".join(self.message)


@dataclass
class GenerateNumber:
    length: int
    seed: Optional[int] = None

    def __post_init__(self):
        if not isinstance(self.length, int) or self.length <= 0:
            raise ValueError("k should be a int positive.")

    def generate(self) -> int:
        if self.seed is not None:
            random.seed(self.seed)
        num = random.choices("1234567890", k=self.length)
        # Asegurar que el primer dígito no sea cero
        while num[0] == '0':
            num = random.choices("1234567890", k=self.length)
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

    def generate(self) -> Key:
        p = self.generate_prime.generate()
        e = self.find_coprime(p - 1)
        d = self.inverse_module(e, p - 1)
        return Key(k1=p, k2=e, k3=d)

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


@dataclass
class StrToInt:
    letters: Letters
    length: int

    def convert(self, message: Message) -> Message:
        new_message = list()
        for line in message.message:
            line_split = [line[self.length*i:(i+1)*self.length]
                          for i in range(len(line)//self.length + 1)]
            number_line_split = [self.str_to_int(
                text=text) for text in line_split]
            number_str_line_split = [self.add_zeros(
                num) for num in number_line_split]
            number_str_line = "".join(number_str_line_split)
            new_message.append(number_str_line)
        return Message(message=new_message)

    def str_to_int(self, text: str) -> int:
        rang = self.letters.range()
        numbers = [self.letters.to_int(letter) if letter in self.letters.KEYS else self.letters.to_int("?")
                   for letter in text]
        num = 0
        for i in range(len(numbers)):
            num += numbers[i] * rang ** int(i)
        return num

    def add_zeros(self, num: int) -> str:
        num_str = str(num)
        while len(num_str) < 2*self.length:
            num_str = "0" + num_str
        return num_str


@dataclass
class IntToStr:
    message: Message
    letters: Letters

    def __post_init__(self):
        for line in self.message.message:
            if not line.is_digits():
                raise ValueError("The line has that have only digits")

    def convert(self) -> Message: ...


@dataclass
class Encryp:
    key: Key
    str_to_int: StrToInt

    def encryp_message(self, message: Message) -> Message:
        length = self.str_to_int.length
        new_message = list()
        code_message = self.str_to_int.convert(message=message)
        for line in code_message.message:
            line_split = []

        print(code_message)

    def encryp(self):
        
        ...


@dataclass
class Decryp:
    key: Key

    def decryp(self, message: Message) -> Message: ...


if __name__ == "__main__":
    GenerateNumber(length=-4)

    try:
        ...
    except:
        input("ERROR")
