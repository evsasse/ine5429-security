from .prng import PRNG

class BBS(PRNG):
	def __init__(self, seed, p, q, bits):
		self.x = seed
		self.m = p * q
		self.bits = bits

	def _PRNG__next(self):
		self.x = pow(self.x, 2) % self.m
		return self.x