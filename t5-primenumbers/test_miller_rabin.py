import unittest
import sympy

from miller_rabin import MillerRabin

class TestMillerRabin(unittest.TestCase):
    def test_d_s(self):
        for n in range(3, 100000):
            d, s = MillerRabin._d_s(n)

            self.assertFalse(d%2 == 0)
            self.assertEqual(d * 2**s, n-1)

    def test_primality_test(self):
        for i in range(3, 100000):
            rr = MillerRabin.test(i)
            self.assertEqual(sympy.isprime(i), rr)

    def test_prime_generator(self):
        mr = MillerRabin(64)
        for _ in range(25):
            generated = mr.next()
            self.assertTrue(sympy.isprime(generated))

if __name__ == '__main__':
    unittest.main()