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
    - Caso alguma transação não chegar em todos os nodos não há problema, em algum
  momento ela será confirmada por um bloco feito por algum dos nodos que recebeu ela,
  e será ela sincronizada aos outros nodos.
3. Cada nodo tentar realizar a prova-de-trabalho com o seu bloco.
4. Quando consegue, envia aos outros nodos o seu bloco.
5. Os outros nodos aceitam o bloco se todas a transações são válidas.
    - Podem ser recebido mais de um novo bloco com prova-de-trabalho válida,
  nesse caso continua se trabalhando com o bloco que foi recebido primeiro.
    - Caso seja recebido um novo bloco que tenha sido originado de uma corrente
  maior, diferente e válida, migra para a nova corrente mais longa.
6. Começam a trabalhar no próximo bloco, com hash do novo bloco recebido/feito.


## 6. Incentivo

Por convenção a primeira transação de um bloco inicializa uma nova moeda que pertencerá
ao quem está tentado criar o bloco. Desse modo novas moedas são adicionadas na economia
e existe um incentivo para que os nodos gastem seu poder computacional.

E também podem haver custos de transação embutidos no sistema, de cada transação de um
bloco é extraido uma taxa é dada ao nodo que criar o novo bloco. Dessa maneira há um
mecanismo para haver incentivos mesmo que não haja mais produção de novas moedas.

Esse mecanismo também incentiva possíveis atacantes, com poder computacional grande, a
tentar criar blocos honestamente ao invés de destruir a economia, já que ele estaria
produzindo uma grande quantidade de moedas.

## 7. Recuperando espaço de armazenamento

Podemos economizar espaço de armazenamento eliminando os dados os dados de transações
muito antigas e armazenando apenas os hash delas, e futuramente armazendo apenas o
hash de um conjunto de hashes de transações... armazenando no final apenas o cabeçalho
do bloco com o hash de hashes ... de transações.

## 8. Verificação de pagamento simplificada

A verificação de pagamento consiste de verificar que a transação que o remetente assinou
contendo a chave pública do destinatário foi confirmada em um bloco da maior corrente.
Pedindo os dados da corrente para outros nodos é confirmado qual a maior corrente, e
buscando a transação nela é verificado se ela foi aceita pela rede. Cada bloco após ao
bloco da transação confirma ainda mais que a transação foi aceita, e não foi apenas parte
de uma corrente temporariamente maior.

Então no caso mais simples o nodo que quer confirmar uma transação não precisa ter um
histórico completo das transações, apenas perguntar para a rede. Mas no caso de um ataque
onde a rede é controlada por um grande número de nodos que podem maleficamente confirmar
uma transação, é interessante que o nodo tenha um histórico completo, podendo confirmar
a transação por si mesmo.


## 9. Combinando e dividindo valores

Para permitir que valores sejam combinados e divididos uma transação permite várias entradas
e até duas saídas. As várias entradas representam os vários valores que serão combinados. E
uma das saídas representa o valor que será pago ao destinatário, enquanto o outro é o valor
de troco devolvido ao remetente.

## 10. Privacidade

A privacidade pode ser mantida simplesmente não associando chaves públicas à identidade de
seus donos. Desse modo as transações podem ser ligadas umas as outras, sem o conhecimento
das identidades. Para aumentar o nível de segurança é interessante que sejam gerados novas
chaves para cada transação, quando possível. Mas existe o risco de que caso a identidade
de alguma chave pública vaze revela outras transações realizadas pelo dono daquela chave.
