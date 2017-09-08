# Geração de números primos

Os seguintes algoritmos foram escolhidos:

- Miller-Rabin (**MR**)
- Teste de Primalidade de Fermat(**Fermat**)
- Lucas Primality Test(**Lucas**)

## Dificuldades

Tive dificuldade em fazer um metodo que fizesse a fatoracao de um numero em seus primos.
Que e necessario no algoritmo de Lucas. Utilizei a funcao da biblioteca sympy, mas mesmo
assim ela nao foi suficientemente performatica para tornar o algoritmo eficiente.

## Tempos de execução

| Algoritmo | #Bits | Primo Gerado | Tempo para gerar |
| --- | --- | --- |
| Miller-Rabin |  40  |  1032706945187  |  0.0013735294342041016 s |
| Fermat |  40  |  238989529039  |  0.0023794174194335938 s |
| Lucas |  40  |  80777871599  |  0.0027306079864501953 s |
| --- | --- | --- |
| Miller-Rabin |  56  |  56526876311970509  |  0.0015053749084472656 s |
| Fermat |  56  |  8723257080296503  |  0.002160310745239258 s |
| Lucas |  56  |  45700179723431017  |  0.0019299983978271484 s |
| --- | --- | --- |
| Miller-Rabin |  80  |  55254998471363037810737  |  0.005181550979614258 s |
| Fermat |  80  |  1111619088234499214728249  |  0.0029397010803222656 s |
| Lucas |  80  |  669834365306796094178687  |  0.004763364791870117 s |
| --- | --- | --- |
| Miller-Rabin |  128  |  61089889084632446803968685153860578209  |  0.007810831069946289 s |
| Fermat |  128  |  121353350587756230017816793245508043777  |  0.0059359073638916016 s |
| --- | --- | --- |
| Miller-Rabin |  168  |  317364360569950129485065407439840504741628836723923  |  0.01401376724243164 s |
| Fermat |  168  |  346580464047305821666792588024929237683969376828317  |  0.06611943244934082 s |
| --- | --- | --- |
| Miller-Rabin |  224  |  26564196922203706299923564945125546021785271826487291575640707850493  |  0.020566225051879883 s |
| Fermat |  224  |  6829371862820391762730736579727911083145277347106782965077464383417  |  0.017734050750732422 s |
| --- | --- | --- |
| Miller-Rabin |  256  |  110863871429052191487195388220749035658985105141384572908096214212511459903411  |  0.07701897621154785 s |
| Fermat |  256  |  24323746804932236073820473702141485805068204930671278217670927743645344932221  |  0.1114962100982666 s |
| --- | --- | --- |
| Miller-Rabin |  512  |  5491493605486946539384845359377230682870607287871332200269323905254309790456054899529174766619811069950689938824650698684597552343924172694229147851581837  |  0.24248361587524414 s |
| Fermat |  512  |  7177989470035277036978680323902845018678237331321144657599674062021959994375794555382404486373451310104828235559868854933576488920901023138448465520902643  |  0.13417649269104004 s |
| --- | --- | --- |
| Miller-Rabin |  1024  |  108866854346904441025885606504463334020368601276829062836592595333757910949813905086095870853392263068537894634103515072526755315571394725322304991229605865064050139914915444046778521093003772266837291249962029765143422598578594222336388363288079648364379849772018686326752810315669189163249873196081409026341  |  5.2607831954956055 s |
| Fermat |  1024  |  45338691288520320018105187056537336480724041310216658885110359111273149349709296183208577759073933970904290540561885173408345321455686481208026511111408173936331682614281670922364765040510537702445504509072332092554570038848769858401451057770751421793974875157023564149188565548457802559019536924969599095271  |  0.47488975524902344 s |
| --- | --- | --- |
| Miller-Rabin |  2048  |  18406376790670584154542192279059700744812504959221943318450912051535763769526623099148547351851996944223713929808863432999722869233429511915908275050471424642989135691634878815983069081113622741768733849287279013049949335886407076626657096155168370056803905287368021813895392314654909094496700421043469999685875777974474413025105062602284950803744037821985216352708535597717262682172662406354182072431986151088408837519816294112828386955402974781047559878789982516682063228648959956033003834450474348463852843263093010025451032086726194534874389267786364122054534471589530793095212764991277019278443147710251086225379  |  93.23341155052185 s |
| Fermat |  2048  |  7595253241945603882230547064311577862814049058895348042123564212700117023528031057159068467055393562021892103990279491033798596685326405949608426866579669150524138720315635106046731781656377255775795113239659941909182378058276935862564448817538031113933747689110697637013935188698082081377071113118098174403756072659424427570294825789504897249029089969479109799593305461105357288657608724343792101888522220330352687937640642838003952031251691971203563065310751737449118955082047264887740966392077585820346141962571537658973025024063254857964384458627516410041085097907338799093590829404110536484758785318435000522179  |  25.661298513412476 s |
| --- | --- | --- |


## Código
**__main.py__**
```
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

```

**miller_rabin.py**
```
import random

from .prime_number_generator import PrimeNumberGenerator

class MillerRabin(PrimeNumberGenerator):
    @staticmethod
    def _d_s(n):
        d = n-1
        s = 0

        while d%2 == 0:
            d = d//2
            s = s+1

        return (d, s)

    @staticmethod
    def _round(n, a, d, s):
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            return True

        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n-1:
                return True

        return False

    @classmethod
    def test(cls, n, k=30):
        assert(n > 1)

        if n == 2 or n == 3:
            return True
        if n%2 == 0:
            return False

        d, s = cls._d_s(n)
     
        for _ in range(k):
            a = random.randrange(2, n-2)
            if not cls._round(n, a, d, s):
                return False
     
        return True
```

**fermat.py**
```
import random

from .prime_number_generator import PrimeNumberGenerator

class Fermat(PrimeNumberGenerator):
    @staticmethod
    def test(n, k=30):
        assert(n > 1)

        if n == 2 or n == 3:
            return True
        if n%2 == 0:
            return False
        
        for _ in range(k):
            a = random.randint(2, n-2)
            x = pow(a, n-1, n)
            if x != 1:
                return False

        return True
```

**lucas.py**
```
import random
import sympy

from .prime_number_generator import PrimeNumberGenerator


class Lucas(PrimeNumberGenerator):
    @classmethod
    def test(cls, n, k=30):
        assert(n > 1)

        if n == 2 or n == 3:
            return True
        if n%2 == 0:
            return False

        factors = cls._prime_factors(n-1)
        
        divided_by_factors = [(n-1)//factor
                              for factor in factors]

        for _ in range(k):
            a = random.randint(2, n-1)

            if pow(a, n-1, n) != 1:
                return False

            for divided in divided_by_factors:
                if pow(a, divided, n) == 1:
                    break
            else:
                return True

        return False

    @staticmethod
    def _prime_factors(n):
        return sympy.primefactors(n)
```

**prime_number_generator.py**
```
from functools import partial
from random import randint

class PrimeNumberGenerator:
    def __init__(self, bits):
        self.bits = bits

    @staticmethod
    def n_iter(bits):
        new_n = partial(randint, 2, 2**bits)

        while True:
            n = new_n()
            
            yield n-1 if n%2 == 0 else n

    def next(self):
        for n in self.n_iter(self.bits):
            if self.test(n):
                return n
```

**timer_decorator.py**
```
import time


def timer(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return (end - start, func(*args, **kwargs))
    return function_timer
```


## Referências utilizadas
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
http://www.javascripter.net/math/primes/millerrabinprimalitytest.htm
https://en.wikipedia.org/wiki/Fermat_primality_test
https://en.wikipedia.org/wiki/Lucas_primality_test
http://docs.sympy.org/latest/index.html

# Disponivel em: https://github.com/evsasse/ine5429-security
