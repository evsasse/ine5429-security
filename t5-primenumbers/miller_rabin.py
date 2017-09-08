import random

from .prime_number_generator import PrimeNumberGenerator

class MillerRabin(PrimeNumberGenerator):
    @staticmethod
    def _d_s(n):
        d = n-1
        s = 0

        while d%2 == 0:
            d = d//2
            s = s+1

        return (d, s)

    @staticmethod
    def _round(n, a, d, s):
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            return True

        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n-1:
                return True

        return False

    @classmethod
    def test(cls, n, k=30):
        assert(n > 1)

        if n == 2 or n == 3:
            return True
        if n%2 == 0:
            return False

        d, s = cls._d_s(n)
     
        for _ in range(k):
            a = random.randrange(2, n-2)
            if not cls._round(n, a, d, s):
                return False
     
        return True
