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

