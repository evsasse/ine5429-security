import unittest
import sympy

from lucas import Lucas

class TestLucas(unittest.TestCase):
    def test_prime_factors(self):
        for n in range(2, 1000):
            self.assertEqual(sympy.primefactors(n), Lucas._prime_factors(n))

    def test_primality_test(self):
        for i in range(3, 1000):
            rr = Lucas.test(i)
            self.assertEqual(sympy.isprime(i), rr)

    def test_prime_generator(self):
        mr = Lucas(64)
        for _ in range(10):
            generated = mr.next()
            self.assertTrue(sympy.isprime(generated))

if __name__ == '__main__':
    unittest.main()