from functools import partial
from random import randint

class PrimeNumberGenerator:
    def __init__(self, bits):
        self.bits = bits

    @staticmethod
    def n_iter(bits):
        new_n = partial(randint, 2, 2**bits)

        while True:
            n = new_n()
            
            yield n-1 if n%2 == 0 else n

    def next(self):
        for n in self.n_iter(self.bits):
            if self.test(n):
                return n