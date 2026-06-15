# Prática 1 – Grafos: Roteamento e Coloração em Redes

Atividade de Grafos aplicada a redes de computadores.

O trabalho está dividido em duas partes:

- `parte1/`: roteamento em rede de backbone.
- `parte2/`: alocação de canais Wi-Fi.

Nesta entrega, foi desenvolvida a **Parte 1**, responsável por encontrar o caminho de menor custo entre dois roteadores em grafos direcionados com pesos.

A Parte 2 será desenvolvida pelo outro integrante da dupla.

---

## Estrutura do repositório

```txt
pratica1-grafos/
├── README.md
├── comparativo.md
├── parte1/
│   ├── roteamento.py
│   ├── grafo_rede_p.txt
│   ├── grafo_rede_m.txt
│   ├── saida_parte1_p.txt
│   └── saida_parte1_m.txt
└── parte2/
    └── .gitkeep
```

---

## Parte 1 – Roteamento em Rede de Backbone

A rede de backbone é representada como um grafo direcionado com pesos.

Cada vértice representa um roteador e cada aresta representa uma conexão entre roteadores com um custo associado.

O objetivo é encontrar o menor caminho entre o roteador de origem e o roteador de destino.

---

## Algoritmos utilizados e justificativa

O programa escolhe automaticamente o algoritmo mais adequado de acordo com os pesos das arestas do grafo.

### Grafo pequeno – `grafo_rede_p.txt`

Para o grafo pequeno, foi utilizado o algoritmo **Dijkstra**.

A escolha foi feita porque todas as arestas possuem pesos não negativos. Nesse caso, o Dijkstra é adequado e eficiente para encontrar o menor caminho.

### Grafo médio – `grafo_rede_m.txt`

Para o grafo médio, foi utilizado o algoritmo **Bellman-Ford**.

A escolha foi feita porque o grafo possui arestas com pesos negativos. O algoritmo de Dijkstra não é indicado para grafos com pesos negativos, pois pode gerar resultados incorretos. O Bellman-Ford suporta pesos negativos e também permite detectar ciclos negativos.

---

## Como executar a Parte 1

É necessário ter o Python 3 instalado.

No terminal, dentro da pasta principal do projeto, execute:

### Grafo pequeno

```bash
python parte1/roteamento.py parte1/grafo_rede_p.txt parte1/saida_parte1_p.txt
```

### Grafo médio

```bash
python parte1/roteamento.py parte1/grafo_rede_m.txt parte1/saida_parte1_m.txt
```

---

## Saída esperada – grafo pequeno

Arquivo gerado: `parte1/saida_parte1_p.txt`

```txt
ALGORITMO: Dijkstra
JUSTIFICATIVA: Todos os pesos das arestas sao nao negativos, portanto Dijkstra e aplicavel e encontra o menor caminho de forma eficiente.
ROTA: 0 1 3 4
CUSTO: 7
```

---

## Saída esperada – grafo médio

Arquivo gerado: `parte1/saida_parte1_m.txt`

```txt
ALGORITMO: Bellman-Ford
JUSTIFICATIVA: O grafo contem arestas com peso negativo, o que invalida Dijkstra. Bellman-Ford suporta pesos negativos e ainda permite detectar ciclos negativos.
ROTA: 0 1 2 4 3 6 9
CUSTO: 6
```

---

## Observação sobre a Parte 2

A Parte 2, referente à coloração de grafos para alocação de canais Wi-Fi, será implementada pelo outro integrante da dupla.

Quando a Parte 2 for adicionada, o README deve ser atualizado com:

- algoritmo utilizado para coloração;
- justificativa da escolha;
- instruções de execução;
- arquivos de saída da Parte 2.

---

## Autoria

- Nelson Alves
- Samuel
