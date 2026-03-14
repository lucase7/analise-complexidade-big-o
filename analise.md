# Análise de Complexidade – Big-O

Disciplina: Estruturas de Dados e Análise de Algoritmos  
Aluno: Lucas Dias  

---

## Exercício 1

### Complexidade
O(1)

### Justificativa
A função apenas acessa o primeiro elemento da lista. O acesso por índice em lista é feito em tempo constante, independentemente do tamanho da entrada.

## Exercício 2

## Complexidade
O(n)

### Justificativa
A função percorre todos os elementos da lista uma única vez usando um loop for. O tempo de execução cresce proporcionalmente ao tamanho da lista.

## Exercício 3 

### Complexidade
O(log n)

### Justificativa
A cada iteração o espaço de busca é reduzido pela metade. Isso caracteriza crescimento logarítmico, típico da busca binária.

## Exercício 4 

### Complexidade
O(n²)

### Justificativa
Há dois loops aninhados que percorrem a lista. Para cada elemento, todos os elementos seguintes são verificados, resultando em comportamento quadrático.

## Exercício 5 

### Complexidade
O(n²)

### Justificativa
O primeiro bloco é O(n), mas o segundo bloco possui dois loops aninhados (O(n²)). Como na análise assintótica consideramos o termo dominante, a complexidade final é O(n²).




