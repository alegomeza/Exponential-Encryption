from math import sqrt
import time


def prime_numbers_generator(max: int = None):
    p = 2
    yield p

    while not max or p < max:
        p = 3
        yield p

        while not max or p+2 <= max:
            is_prime = True
            p += 2
            for number in range(2, int(sqrt(p)) + 1):
                if p % number == 0:
                    is_prime = False
                    break
            if is_prime:
                yield p
        break


def run():
    f = prime_numbers_generator()
    for i in f:
        print(i)
        time.sleep(0.05)


if __name__ == '__main__':
    run()
