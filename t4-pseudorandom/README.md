# Geração de números Pseudo-aleatórios

Foram escolhidos os algoritmos, eles são muito parecidos,
mudando poucos detalhes de como o próximo número da sequência(**x<sub>k+1</sub>**) é gerado.

Segue as fórmulas e dados que foram utilizados para escolher as
entradas dos algoritmos.

- Blum Blum Shub (**BBS**)

  ![Formula bbs](http://i.imgur.com/1bbH3VZ.png)
  
  Onde, **M = p * q**, e p e q são números primos.
  E a seed(**x<sub>0</sub>**) é co-primo de **M**.
  
- Linear congruential generator (**LCG**)

  ![Formula lgc](http://i.imgur.com/Kq0qnb7.png)
  
  Onde, **m** e **x** são relativamente primos;
  **a - 1** é divisivel por todos os fatores de **m**;
  **a - 1** é divisivel por **4** se **m** é divisivel por **4**.
  Escolhendo **m** e **a** como números primos, evitei qualquer conflito com isso.
  
- Park–Miller random number generator (**PM**)

  ![Formula pm](http://i.imgur.com/UgqsOHZ.png)
  
  Onde, **n** é um número primo, e **g** escolhido como uma raiz primitiva de **n**.
  E a seed(**x<sub>0</sub>**) é co-primo de **n**.

Eles são muito parecidos, mas para gerar números de um tamanho específico, **B** em bits,
é necessário mudar os paramêtros utilizados, apesar de utilizarem o mesmo algoritmo.

Utilizei então o método de seleção que é apresentado nas referências do Blum blum shub.
Onde gero uma sequência de **B** números(cada chamada de "__next"),
e utilizo cada um deles para se tornar apenas um bit
na saída real do algoritmo. (Realizado na função "next").

## Tempos de execução

| Algoritmo | Tamanho do Número | Tempo para gerar |
| --- | --- | --- |
| BBS |  40  |  7.323980331420898e-05 s |
| LCG |  40  |  8.888006210327149e-05 s |
| PM |  40  |  9.27734375e-05 s |
| --- | --- | --- |
| BBS |  56  |  0.0001253199577331543 s |
| LCG |  56  |  0.0001079702377319336 s |
| PM |  56  |  0.0001321697235107422 s |
| --- | --- | --- |
| BBS |  80  |  0.00018508195877075194 s |
| LCG |  80  |  0.0002047109603881836 s |
| PM |  80  |  0.00015939235687255859 s |
| --- | --- | --- |
| BBS |  128  |  0.00029066085815429685 s |
| LCG |  128  |  0.00024224042892456054 s |
| PM |  128  |  0.0002685999870300293 s |
| --- | --- | --- |
| BBS |  168  |  0.00038299798965454104 s |
| LCG |  168  |  0.00035654067993164064 s |
| PM |  168  |  0.0003596806526184082 s |
| --- | --- | --- |
| BBS |  224  |  0.0004924678802490234 s |
| LCG |  224  |  0.0004644918441772461 s |
| PM |  224  |  0.0004905080795288086 s |
| --- | --- | --- |
| BBS |  256  |  0.0005728507041931152 s |
| LCG |  256  |  0.0005713200569152832 s |
| PM |  256  |  0.0005492091178894043 s |
| --- | --- | --- |
| BBS |  512  |  0.0010515689849853516 s |
| LCG |  512  |  0.0011067390441894531 s |
| PM |  512  |  0.0010668802261352538 s |
| --- | --- | --- |
| BBS |  1024  |  0.002099788188934326 s |
| LCG |  1024  |  0.0021180009841918947 s |
| PM |  1024  |  0.002266988754272461 s |
| --- | --- | --- |
| BBS |  2048  |  0.00438431978225708 s |
| LCG |  2048  |  0.004356811046600342 s |
| PM |  2048  |  0.004405350685119629 s |
| --- | --- | --- |
| BBS |  4096  |  0.009260921478271485 s |
| LCG |  4096  |  0.00937819004058838 s |
| PM |  4096  |  0.00922947883605957 s |

## Código

**__main__.py**
```
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
```

**timer_decorator.py**
```
import time


def timer(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return function_timer
```

**prngs/blum_blum_shub.py**
```
from .prng import PRNG

class BBS(PRNG):
	def __init__(self, seed, p, q, bits):
		self.x = seed
		self.m = p * q
		self.bits = bits

	def _PRNG__next(self):
		self.x = pow(self.x, 2) % self.m
		return self.x
 ```
 
 **prngs/linear_congruential.py**
```
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
 ```
 
**prngs/linear_congruential.py**
```
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
 ```
 
**prngs/prng.py**
```
class PRNG:
	def next(self):
		out = 0

		for _ in range(self.bits):
			out = (out << 1) | self.__selection(self.__next())

		return out
		
	def __selection(self, number):
		# least significant bit
		return number & 1
 ```
 

## Referências
https://en.wikipedia.org/wiki/Blum_Blum_Shub
https://en.wikipedia.org/wiki/Lehmer_random_number_generator
https://en.wikipedia.org/wiki/Linear_congruential_generator

## Disponivel em: https://github.com/evsasse/ine5429-security
