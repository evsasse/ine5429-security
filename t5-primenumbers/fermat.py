import random

from .prime_number_generator import PrimeNumberGenerator

class Fermat(PrimeNumberGenerator):
    @staticmethod
    def test(n, k=30):
        assert(n > 1)

        if n == 2 or n == 3:
            return True
        if n%2 == 0:
            return False
        
        for _ in range(k):
            a = random.randint(2, n-2)
            x = pow(a, n-1, n)
            if x != 1:
                return False

        return True
