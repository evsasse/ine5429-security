# Bitcoin: sistema eletrônico de dinheiro peer-to-peer

Uma solução para transações de dinheiro eletrônico que evita ter
que passar por uma instituição ou terceiro confiável.
Hashes das transações são adicionadas em uma corrente,
e a maior corrente é sempre formada pelo maior poder de processamento.
A maior corrente é aceita como a versão real das transações que
ocorrem. Um conjunto de poder de processamento menor que esteja
tentando atacar a corrente sempre será ultrapassado pelo resto
que conseguirá criar uma corrente maior.

## 1. Introdução

Eliminando a instituição/terceiro confiável que até o momento é necessário
para realizar comércio na internet diminuimos os custos de transação e
a possibilidade de fraudes que utilizam os mecanismos de reverter transações.

Precisamos de um sistema que utiliza provas criptográficas no lugar da confiança
de modo a proteger os compradores e os vendedores. Com um sistema peer-to-peer
que gera a provas criptográficas da ordem das transações, temos segurança
enquanto os número de nodos honestos na rede é maior que tamanho de cada grupo 
de nodos que estão cooperando para atacar.


## 2. Transações

Cada moeda digital é composta de uma corrente de assinaturas digitais. Em uma
transação o remetente assina(com sua chave privada) um hash da última
transação(que tem a mesmo formato do resultado final dessa) e a
chave pública do destinatário e adiciona isso ao final da corrente da moeda.
Assim podemos verificar a cadeia de posse dessa moeda.

Existe a possibilidade de que o remetente tenha feito esse processo para dois
destinatários diferentes, e o destinatário não teria como saber disso apenas
vendo a cadeia de posse que lhe foi entregue. Para combater, isso sem requerer
uma autoridade confiável, as transações são publicamente anunciadas e os
participantes da rede acabam decidindo "chegou primeiro", acordando em qual
o histórico de transações correto. O destinatário então tem que confirmar qual
foi o histórico acordado para confirmar que a transação dada pelo remetente
foi oficializada.

## 3. Servidor de Timestamp

É realizado um hash do timestamp anterior junto ao um bloco de items, o
resultado desse hash é o novo timestamp, que é então publicado, provando que
em algum momento as informações daquele bloco foram confirmadas pois essa
seria a "única" possibilidade, de histórico de transações, que levaria ao
timestamp atual.

## 4. Prova-de-trabalho

Fazemos o hash da prova-de-trabalho anterior junto com cada transação que estará
contida nesse bloco e um número qualquer que será mudado até obtermos o resultado
que procuramos. O resultado desejado é que o hash resultante tenha uma certo número
de zeros como primeiros bits, para alcançar isso temos o número variável dentro do
bloco. Se qualquer coisa dentro do bloco mudar, o hash resultante é completamente
diferente, invalidando o trabalho anterior.

Essa prova-de-trabalho é uma maneira de confirmar que uma certa quantidade de poder
de processamento foi gasto, quanto maior a sua capacidade de processamento então
maior o seu "poder de voto" na corrente. Qualquer poder de processamento menor que
chegasse primeiro no resultado para por um bloco falso na corrente iria ser acabar
ultrapassado pelo tamanho da corrente dos nodos honestos, que não aceitariam esse
bloco falso, nos blocos subsequentes.

E a dificuldade, estabelecida pelo número de zeros que o hash resultante deve começar,
aumenta de forma a obedecer uma média móvel. Mantendo o número de blocos/hora estável.

## 5. Rede

1. Novas transações são publicadas para os outros nodos.
2. Cada nodo coleta as transações que recebe em um bloco.
    - Caso uma transação não chegar em todos os nodos não há problema, em algum
  momento ela será confirmada por um bloco feito por algum dos nodos que recebeu,
  e será sincronizada aos outros nodos.
3. Cada nodo tentar realizar a prova-de-trabalho com o seu bloco.
4. Quando consegue, envia aos outros nodos o seu bloco.
5. Os outros nodos aceitam o bloco se todas a transações são válidas.
    - Podem ser recebido mais de um novo bloco com prova-de-trabalho válida,
  nesse caso continua se trabalhando com o bloco que foi recebido primeiro.
    - Caso seja recebido um novo bloco que tenha sido originado de uma corrente
  maior, diferente e válida, migra para a nova corrente mais longa.
6. Começam a trabalhar no próximo bloco, com hash do novo bloco recebido/feito.
