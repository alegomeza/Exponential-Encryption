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

    @property
    def range(self):
        return len(self.KEYS)

    def to_int(self, value: str) -> int:
        dict_prov = {self.KEYS[idx]: int(idx) for idx in range(self.range)}
        return dict_prov[value]

    def to_str(self, value: int) -> str:
        dict_prov = {int(idx): self.KEYS[idx] for idx in range(self.range)}
        return dict_prov[value]


@dataclass
class Key:
    k1: int
    k2: int
    k3: int

    @property
    def length(self) -> int:
        return len(str(self.k1))

    def convert(self, num: int, mode: str = "encrypt"):
        mod = self.k1
        if mode == "encrypt":
            exp = self.k2
        elif mode == "decrypt":
            exp = self.k3
        else:
            raise ValueError(
                f"{mode} is not a mode.\nmode: \"encrypt\" | \"decrypt\"")
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

    def generate_number(self) -> int:
        if self.seed is not None:
            random.seed(self.seed)
        num = random.choices("1234567890", k=self.length)
        # Asegurar que el primer dígito no sea cero
        while num[0] == '0':
            num = random.choices("1234567890", k=self.length)
        num = "".join(num)
        return int(num)


@dataclass
class GeneratePrime(GenerateNumber):

    def generate_prime(self) -> int:
        while True:
            p = self.generate_number()
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

    length: int

    def generate(self) -> Key:
        p = self.generate_prime()
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
            n = self.generate_number()
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

    def generate_prime(self):
        gen_prime = GeneratePrime(length=self.length)
        return gen_prime.generate_prime()

    def generate_number(self):
        gen_number = GenerateNumber(length=self.length-1)
        return gen_number.generate_number()


@dataclass
class StrToInt:
    letters: Letters

    def convert(self, text: str) -> int:
        rang = self.letters.range
        numbers = [self.letters.to_int(letter) if letter in self.letters.KEYS else self.letters.to_int("?")
                   for letter in text]
        num = 0
        for i in range(len(numbers)):
            num += numbers[i] * rang ** int(i)
        return num


@dataclass
class IntToStr:
    letters: Letters

    def convert(self, num: int) -> str:
        text = str()
        rang = self.letters.range
        r, div = 1, 1
        while div != 0:
            div = num // rang
            r = num % rang
            num = div
            text += self.letters.to_str(r)
        return text


@dataclass
class SplitJoinLine:
    length: int

    def join(self, line_split: List[str]) -> List[str]:
        return "".join(line_split)
        ...

    def split(self, line: str) -> List[str]:
        return [line[self.length*i:(i+1)*self.length]
                for i in range((len(line) - 1)//self.length + 1)]

    def add_zeros(self, num: int) -> str:
        num_str = str(num)
        while len(num_str) < 2*self.length:
            num_str = "0" + num_str
        return num_str


@dataclass
class Encryp:
    key: Key
    str_to_int: StrToInt
    int_to_str: IntToStr

    def encryp_message(self, message: Message) -> Message:
        cypher_message = list()
        length = self.key.length - 1
        split_join = SplitJoinLine(length)
        for line in message.message:
            print(f"{line=}")
            number_line = self._to_int(line)
            print(f"{number_line=}")
            number_str_line = str(number_line)
            print(f"{number_str_line=}")
            number_str_line_split = split_join.split(number_str_line)
            print(f"{number_str_line_split=}")
            number_line_split = [int(number) for number in number_str_line_split]
            print(f"{number_line_split=}")
            cypher_number_line_split = self._to_encrypt(number_line_split)
            print(f"{cypher_number_line_split=}")
            cypher_number_str_line_split = self._add_zeros(cypher_number_line_split)
            print(f"{cypher_number_str_line_split=}")
            cypher_number_str_line = split_join.join(cypher_number_str_line_split)
            print(f"{cypher_number_str_line=}")
            cypher_number_line = int(cypher_number_str_line)
            print(f"{cypher_number_line=}")
            cypher_line = self._to_str(cypher_number_line)
            print(f"{cypher_line=}")
            cypher_message.append(cypher_line)
            print(f"{cypher_message=}")
        return Message(cypher_message)
    
    def decryp_message(self, cypher_message: Message) -> Message:
        message = list()
        length = self.key.length
        split_join = SplitJoinLine(length)        
        for cypher_line in cypher_message.message:
            print(f"{cypher_line=}")
            cypher_number_line = self._to_int(cypher_line)
            print(f"{cypher_number_line=}")
            cypher_number_str_line = str(cypher_number_line)
            print(f"{cypher_number_str_line=}")
            cypher_number_str_line_split = split_join.split(cypher_number_str_line)
            print(f"{cypher_number_str_line_split=}")
            cypher_number_line_split = self._list_str_to_int(cypher_number_str_line_split)
            print(f"{cypher_number_line_split=}")
            number_line_split = self._to_decrypt(cypher_number_line_split)
            print(f"{number_line_split=}")
            number_str_line_split = self._add_zeros(number_line_split)
            print(f"{number_str_line_split=}")
            # number_str_line_split = self._list_int_to_str(number_line_split)
            number_str_line = split_join.join(number_str_line_split)
            print(f"{number_str_line=}")
            number_line = int(number_str_line)
            print(f"{number_line=}")
            line = self._to_str(number_line)
            print(f"{line=}")
            message.append(line)
            print(f"{message=}")
        return Message(message)


    def _to_int(self, line: str) -> int:
        return self.str_to_int.convert(line)
    
    def _to_str(self, line: int) -> str:
        return self.int_to_str.convert(line)

    def _to_encrypt(self, number_line_split: List[int]) -> List[int]:
        return [self.key.convert(num=number, mode="encrypt")
                for number in number_line_split]

    def _to_decrypt(self, number_line_split: List[int]) -> List[int]:
        return [self.key.convert(num=number, mode="decrypt")
                for number in number_line_split]
        
    def _add_zeros(self, number_line_split: List[int]) -> List[str]:
        return [self._zeros(num) for num in number_line_split]
        
    def _zeros(self, num: int) -> str:
        num_str = str(num)
        while len(num_str) < self.key.length:
            num_str = "0" + num_str
        return num_str
    
    def _list_str_to_int(self, number_str_line_split: List[str]) -> List[int]:
        return [int(number) for number in number_str_line_split]
    
    def _list_int_to_str(self, number_line_split: List[str]) -> List[str]:
        return [str(number) for number in number_line_split]        
        


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
        
# Sebastián Alejandro Gómez Ardila

#  #################### 

# Key(k1=1409, k2=769, k3=769)

#  ####################

# line='Sebastián Alejandro Gómez Ardila'
# number_line=76747180370329892177287290112450270374829442316474700438594099
# number_str_line='76747180370329892177287290112450270374829442316474700438594099'
# number_str_line_split=['767', '471', '803', '703', '298', '921', '772', '872', '901', '124', '502', '703', '748', '294', '423', '164', '747', '004', '385', '940', '99']
# number_line_split=[767, 471, 803, 703, 298, 921, 772, 872, 901, 124, 502, 703, 748, 294, 423, 164, 747, 4, 385, 940, 99]
# cypher_number_line_split=[847, 19, 760, 593, 1027, 932, 27, 67, 939, 1233, 1151, 593, 592, 1394, 408, 418, 1134, 25, 154, 1131, 952]
# cypher_number_str_line_split=['0847', '0019', '0760', '0593', '1027', '0932', '0027', '0067', '0939', '1233', '1151', '0593', '0592', '1394', '0408', '0418', '1134', '0025', '0154', '1131', '0952']
# cypher_number_str_line='084700190760059310270932002700670939123311510593059213940408041811340025015411310952'
# cypher_number_line=84700190760059310270932002700670939123311510593059213940408041811340025015411310952
# cypher_line='%Ó.JZwG)"{rnc(*E;}¿¿tk@qlÓ#UTRWLÍsÍj{DiGÉ L'
# cypher_message=['%Ó.JZwG)"{rnc(*E;}¿¿tk@qlÓ#UTRWLÍsÍj{DiGÉ L']
# %Ó.JZwG)"{rnc(*E;}¿¿tk@qlÓ#UTRWLÍsÍj{DiGÉ L

#  ####################

# cypher_line='%Ó.JZwG)"{rnc(*E;}¿¿tk@qlÓ#UTRWLÍsÍj{DiGÉ L'
# cypher_number_line=84700190760059310270932002700670939123311510593059213940408041811340025015411310952
# cypher_number_str_line='84700190760059310270932002700670939123311510593059213940408041811340025015411310952'
# cypher_number_str_line_split=['8470', '0190', '7600', '5931', '0270', '9320', '0270', '0670', '9391', '2331', '1510', '5930', '5921', '3940', '4080', '4181', '1340', '0250', '1541', '1310', '952']
# cypher_number_line_split=[8470, 190, 7600, 5931, 270, 9320, 270, 670, 9391, 2331, 1510, 5930, 5921, 3940, 4080, 4181, 1340, 250, 1541, 1310, 952]
# number_line_split=[625, 483, 985, 118, 675, 756, 675, 266, 1079, 1184, 279, 1394, 1017, 1194, 3, 827, 1330, 40, 1180, 457, 99]
# number_str_line_split=['0625', '0483', '0985', '0118', '0675', '0756', '0675', '0266', '1079', '1184', '0279', '1394', '1017', '1194', '0003', '0827', '1330', '0040', '1180', '0457', '0099']
# number_str_line='062504830985011806750756067502661079118402791394101711940003082713300040118004570099'
# number_line=62504830985011806750756067502661079118402791394101711940003082713300040118004570099
# line="AnfVIVññ?mVsé'EH¿Z¿WD%íqHcqS]ÉLT&fáYÚ;kC{cI"
# message=["AnfVIVññ?mVsé'EH¿Z¿WD%íqHcqS]ÉLT&fáYÚ;kC{cI"]
# AnfVIVññ?mVsé'EH¿Z¿WD%íqHcqS]ÉLT&fáYÚ;kC{cI

#  ####################
