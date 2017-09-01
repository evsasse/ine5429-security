from .prng import PRNG

class PM(PRNG):
	def __init__(self, seed, n, g, bits):
		self.x = seed
		self.n = n
		self.g = g
		self.bits = bits

	def _PRNG__next(self):
		self.x = (self.g * self.x) % self.n
		return self.x