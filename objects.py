import random
from dataclasses import dataclass
from dotenv import load_dotenv


class GeneratePrime:
    ...


@dataclass
class Message:
    message: str


@dataclass
class Key:
    k1: int
    k2: int
    k3: int


@dataclass
class Encryp:
    key: Key

    def encryp(self, message: Message) -> Message: ...


@dataclass
class Decryp:
    key: Key

    def decryp(self, message: Message) -> Message: ...
    
if __name__ == "__main__":
    ...
