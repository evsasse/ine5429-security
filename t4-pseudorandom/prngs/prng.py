class PRNG:
	def next(self):
		out = 0

		for _ in range(self.bits):
			out = (out << 1) | self.__selection(self.__next())

		return out
		
	def __selection(self, number):
		# least significant bit
		return number & 1