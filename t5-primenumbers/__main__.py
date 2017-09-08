from .miller_rabin import MillerRabin
from .fermat import Fermat
from .lucas import Lucas

from .timer_decorator import timer

BITS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

BITS_MR = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
BITS_FERMAT = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
BITS_LUCAS = [40, 56, 80]

REPS = 1

def main():
    print('| Algoritmo | #Bits | Primo Gerado | Tempo para gerar |')

    for bits in BITS:
        print('| --- | --- | --- |')
        mr = MillerRabin(bits)
        # mr_primes = [mr.next(), mr.next() , ...]
        fermat = Fermat(bits)
        lucas = Lucas(bits)

        if bits in BITS_MR:

            t_mr, results_mr = repeat_next(mr, REPS)
            print('| Miller-Rabin | ', bits, ' | ', results_mr[0], ' | ', t_mr / REPS, 's |')

        if bits in BITS_FERMAT:
            t_fermat, results_fermat = repeat_next(mr, REPS)
            print('| Fermat | ', bits, ' | ', results_fermat[0], ' | ', t_fermat / REPS, 's |')

        if bits in BITS_LUCAS:
            t_lucas, results_lucas = repeat_next(mr, REPS)
            print('| Lucas | ', bits, ' | ', results_lucas[0], ' | ', t_lucas / REPS, 's |')

@timer
def repeat_next(algo, times):
    return [algo.next() for _ in range(times)]

if __name__ == "__main__":
    main()
