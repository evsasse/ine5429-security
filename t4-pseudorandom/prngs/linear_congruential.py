from .prng import PRNG

class LCG(PRNG):
	def __init__(self, seed, m, c, bits):
		self.x = seed
		self.m = m
		self.a = c
		self.c = c
		self.bits = bits

	def _PRNG__next(self):
		self.x = (self.a * self.x + self.c) % self.m
		return self.x