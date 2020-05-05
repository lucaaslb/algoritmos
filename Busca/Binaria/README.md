# Busca Binaria

A busca binaria é um algoritmo. Sua entrada é uma lista/array de dados ORDENADOS e um elemento a ser buscado. Se o elemento que esta sendo buscado está na lista, a pesquisa retorna a sua posição no array. Caso contrario é retornado Null/None ou uma posição inexistente como por exemplo -1. 

> Elimine metade do números a cada tentativa com a pesquisa binária. 

O algoritmo funciona da seguinte maneira: Recebendo uma lista ordenada, temos como base posições de valores menores e maiores. Então quando busco o valor o algoritmo consegue saber se o valor é menor ou maior comparando com o valor da posição do meio da lista. Então caso não encontre de primeira, a lista é quebrada pela metade para utilizar apenas as posições onde o valor buscado possa estar. 

Exemplo comparando com uma busca sequencial retirado do livro ["Entendendo Algoritmos: Um guia ilustrado para programadores e outros curiosos"](https://www.amazon.com.br/dp/B07B61HC3L/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1):

> Suponha que você esteja procurando uma palavra em um dicionario. O Dicionairo tem 240.000 palavras. No pior dos casos, se a palavra estiver na ultima posição, uma busca sequencial levaria 240.000 etapas para encontrar.  
> Na busca binária, a cada etapa é eliminado metade ate que reste apenas uma palavra e nesse mesmo caso, a busca binária levaria apenas 18 etapas. 

A Busca Sequêncial em tempo de execução *__O(n)__*, sendo *__n__* o numero de elementos.   
A Busca Binaria possui o tempo de execução *__O(log n)__*.
<p align="center">
  <img src="https://github.com/lucaaslb/algoritmos/blob/master/img/big-o.jpg">
</p>


__Implementação__ de forma iterativa e recursiva:   
- [Python](busca_binaria.py)  
- [Java](BuscaBinaria.java)

#### Referências:
+ [Entendendo Algoritmos: Um guia ilustrado para programadores e outros curiosos](https://www.amazon.com.br/dp/B07B61HC3L/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
+ [Khan Academy](https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)


___
:beer: :pizza: