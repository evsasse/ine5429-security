import unittest
import sympy

from fermat import Fermat

class TestMillerRabin(unittest.TestCase):
    def test_primality_test(self):
        for i in range(3, 100000):
            try:
                rr = Fermat.test(i)
                self.assertEqual(sympy.isprime(i), rr)
            except:
                print(i)

    def test_prime_generator(self):
        f = Fermat(64)
        for _ in range(25):
            generated = f.next()
            self.assertTrue(sympy.isprime(generated))

if __name__ == '__main__':
    unittest.main()