import random
import sympy

from .prime_number_generator import PrimeNumberGenerator


class Lucas(PrimeNumberGenerator):
    @classmethod
    def test(cls, n, k=30):
        assert(n > 1)

        if n == 2 or n == 3:
            return True
        if n%2 == 0:
            return False

        factors = cls._prime_factors(n-1)
        
        divided_by_factors = [(n-1)//factor
                              for factor in factors]

        for _ in range(k):
            a = random.randint(2, n-1)

            if pow(a, n-1, n) != 1:
                return False

            for divided in divided_by_factors:
                if pow(a, divided, n) == 1:
                    break
            else:
                return True

        return False

    @staticmethod
    def _prime_factors(n):
        return sympy.primefactors(n)