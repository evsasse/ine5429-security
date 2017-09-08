from .prngs.blum_blum_shub import BBS
from .prngs.park_miller import PM
from .prngs.linear_congruential import LCG


BITS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
REPS = 5

def main():
	for bits in BITS:
		ALGOS = [BBS(SEED, P_PRIME, Q_PRIME, bits),
		 	     PM(SEED, P_PRIME, P_PRIMITIVE_ROOT, bits)]

		prng = LCG(SEED, P_PRIME, Q_PRIME, bits)
		for _ in range(REPS):
			print(bits, prng.next())
		print('---------------')

if __name__ == "__main__":
	main()