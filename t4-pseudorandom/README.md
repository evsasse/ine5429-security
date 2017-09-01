# Geração de números Pseudo-aleatórios

Foram escolhidos os algoritmos, eles são muito parecidos,
mudando poucos detalhes de como o próximo número da sequência(**x<sub>k+1</sub>**) é gerado.

Segue as fórmulas e dados que foram utilizados para escolher as
entradas dos algoritmos.

- Blum Blum Shub

  ![Formula bbs](http://i.imgur.com/1bbH3VZ.png)
  
  Onde, **M = p * q**, e p e q são números primos.
  E a seed(**x<sub>0</sub>**) é co-primo de **M**.
  
- Linear congruential generator

  ![Formula lgc](https://wikimedia.org/api/rest_v1/media/math/render/svg/70a1708a4432a26fa32571271104f9caabdefc1c)
  
  Onde, **m** e **x** são relativamente primos;
  **a - 1** é divisivel por todos os fatores de **m**;
  **a - 1** é divisivel por **4** se **m** é divisivel por **4**.
  Escolhendo **m** e **a** como números primos, evitei qualquer conflito com isso.
  
- Park–Miller random number generator

  ![Formula pm](https://wikimedia.org/api/rest_v1/media/math/render/svg/2b963c8f17e4030a9594bd39a9f528f7b64ddd4f)
  
  Onde, **n** é um número primo, e **g** escolhido como uma raiz primitiva de **n**.
  E a seed(**x<sub>0</sub>**) é co-primo de **n**.

Eles são muito parecidos, mas para gerar números de um tamanho específico, **B** em bits,
é necessário mudar os paramêtros utilizados, apesar de utilizarem o mesmo algoritmo.

Utilizei então o método de seleção que é apresentado nas referências do Blum blum shub.
Onde gero uma sequência de **B** números(cada chamada de "__next"),
e utilizo cada um deles para se tornar apenas um bit
na saída real do algoritmo. (Realizado na função "next").

