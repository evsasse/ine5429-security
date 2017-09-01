from .prngs.blum_blum_shub import BBS
from .prngs.park_miller import PM
from .prngs.linear_congruential import LCG

from .timer_decorator import timer


SEED = 2

P_PRIME = 3141592653589771
Q_PRIME = 2718281828459051

P_PRIMITIVE_ROOT = 3

BITS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
REPS = 100


def main():
    print('| Algoritmo | Tamanho do Número | Tempo para gerar |')
    print('| --- | --- | --- |')
    for bits in BITS:
        bbs = BBS(SEED, P_PRIME, Q_PRIME, bits)
        # random_bbs_numbers = [bbs.next(), bbs.next()]
        lcg = LCG(SEED, P_PRIME, Q_PRIME, bits)
        # random_lcg_numbers = [lcg.next(), lcg.next()]
        pm = PM(SEED, P_PRIME, P_PRIMITIVE_ROOT, bits)
        # random_pm_numbers = [pm.next(), pm.next()]

        print('| BBS | ', bits, ' | ', repeat_next(bbs, REPS) / REPS, 's |')
        print('| LCG | ', bits, ' | ', repeat_next(bbs, REPS) / REPS, 's |')
        print('| PM | ', bits, ' | ', repeat_next(bbs, REPS) / REPS, 's |')

        print('| --- | --- | --- |')


@timer
def repeat_next(algo, times):
    for _ in range(times):
        algo.next()

if __name__ == "__main__":
    main()
