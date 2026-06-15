# Comparativo dos Algoritmos da Parte 1

## Objetivo

Comparar os algoritmos utilizados na Parte 1 da atividade, considerando as características dos dois grafos de entrada.

---

## Grafo pequeno – `grafo_rede_p.txt`

No grafo pequeno, todos os pesos das arestas são não negativos.

Por isso, o algoritmo escolhido foi o **Dijkstra**.

O Dijkstra é adequado para esse caso porque encontra o menor caminho de forma eficiente quando não existem arestas com peso negativo.

Resultado encontrado:

```txt
ROTA: 0 1 3 4
CUSTO: 7
```

---

## Grafo médio – `grafo_rede_m.txt`

No grafo médio, existem arestas com peso negativo.

Por isso, o algoritmo escolhido foi o **Bellman-Ford**.

O Dijkstra não é indicado para grafos com pesos negativos, pois pode produzir resultados incorretos. Já o Bellman-Ford suporta pesos negativos e também verifica a existência de ciclos negativos alcançáveis a partir da origem.

Resultado encontrado:

```txt
ROTA: 0 1 2 4 3 6 9
CUSTO: 6
```

---

## Conclusão

A escolha dos algoritmos depende diretamente das características dos pesos das arestas.

Quando todos os pesos são não negativos, o Dijkstra é uma boa escolha por ser eficiente.

Quando existem pesos negativos, o Bellman-Ford é mais adequado, pois trata corretamente esse tipo de grafo.
