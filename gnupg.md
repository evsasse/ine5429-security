# GNUPG
GnuPG(GNU Privacy Guard), também conhecido como GPG, é uma implementação, sob a licença GPL, do padrão OpenPGP, que por sua vez é um padrão aberto baseado no programa PGP(Pretty Good Privacy).
Esse padrão é comumente usado para assinaturas digitais, ciframento, compressão, gerenciamento de chaves e certificados.
E para suportar esses usos possui implementações de diversos algoritmos de: chaves assimétricas, como RSA e DSA; chaves simétricas, como AES e BLOWFISH; compressão, como ZIP e ZLIB; e hash, como MD5 e SHA1.
A interface usual do GnuPG é através da linha de comando, mas existem diversas integrações e bibliotecas que facilitam o uso para os programas, inclusive com suporte à Windows.

Atualmente a última versão do GnuPG é a 2.1.23 e é candidata a se tornar a versão 2.2.0 que terá suporte a longo prazo. Exemplo desse suporte é que atualizações para versões legadas ainda são lançadas, possibilitando que desenvolvedores atualizem e se protejam de alguns novos ataques mesmo que não possam atualizar para a última versão, por problemas de compatibilidade.

A geração de chaves públicas e privadas é suportada pelo GnuPG, assim como cifrar e decifrar dados utilizando dessas chaves, e portanto o GnuPG é uma escolha comum de ferramenta em situações de usam esse tipo de cifra.
Expondo uma chave pública você permite que terceiros possam decifrar mensagens por você, verificar que mensagens enviadas por você são verdadeiras através de uma assinatura, ou que enviem mensagens cifradas que apenas você conseguirá decifrar com a sua chave privada.
Então, trocando chaves públicas com seus colegas vocês poderiam trocar arquivos e conversas que apenas vocês teriam acesso.
Um uso comum disso que é amplamente suportado pela comunidade do GnuPG é na proteção de emails, mandando a sua chave pública para um "keyserver" você pode cifrar as suas mensagens, em um cliente de email que suporte isso, e conversar com outras pessoas que também tenha feito upload da chave pública delas.
O processo de importação e exportação de chaves para os "keyservers" também são funcionalidades do GnuPG
O GnuPG também suporta a possibilidade de que um dado tenha vários destinatários, possuindo a chave pública desses destinatários você pode construir um arquivo que pode ser decifrado por qualquer uma das chaves privadas deles.

Um processo importante em que o GnuPG também é utilizado é a revocação de chaves. Caso sua chave privada seja descoberta, ou simplesmente você quer criar uma nova chave e destituir a anterior, você pode realizar o processo de revocação de chave. Para isso é necessário que seja gerado um certificado de revocação, esse processo requer que você tenha acesso a sua chave privada original. Isso pode ser feito pelo GnuPG, e é até recomendado que você gere o certificado de revocação logo após a geração das suas chaves, você pode mantê-lo guardado e nunca precisar usar, mas caso você perca a sua chave privada você não conseguiria gerá-lo.
