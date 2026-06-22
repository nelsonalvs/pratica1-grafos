# Prática 1 – Grafos: Roteamento e Coloração em Redes

Atividade de Grafos aplicada a redes de computadores.

O trabalho está dividido em duas partes:

- `parte1/`: roteamento em rede de backbone.
- `parte2/`: alocação de canais Wi-Fi.

O trabalho está dividido entre os três integrantes da equipe:

- **Nelson Alves** - Parte 1: roteamento com Dijkstra e Bellman-Ford
- **Francys Samuel** - Parte 2: coloração gulosa para o grafo pequeno
- **Lucas Fernando** - Parte 2: coloração DSatur para o grafo médio

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
    ├── coloracao_guloso.py
    ├── coloracao_dsatur.py
    ├── grafo_wifi_p.txt
    ├── grafo_wifi_m.txt
    ├── saida_parte2_p.txt
    └── saida_parte2_m.txt
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

---

## Parte 2 – Alocação de Canais Wi-Fi

A rede Wi-Fi é representada como um grafo não-direcionado sem pesos.

Cada vértice representa um ponto de acesso (AP) e cada aresta indica interferência mútua entre dois APs. APs adjacentes não podem usar o mesmo canal.

O objetivo é colorir o grafo com o menor número possível de cores (número cromático).

---

## Algoritmos utilizados e justificativa

### Grafo pequeno – `grafo_wifi_p.txt`

Foi utilizado o algoritmo **Guloso**.

O algoritmo percorre os vértices em ordem e atribui a cada um a menor cor que não conflite com os vizinhos já coloridos. Para o grafo pequeno, esse método encontra a solução ótima de forma simples e eficiente.

### Grafo médio – `grafo_wifi_m.txt`

Foi utilizado o algoritmo **DSatur**.

O DSatur escolhe a cada passo o vértice com maior grau de saturação (número de cores distintas já usadas pelos vizinhos), produzindo colorações próximas ao ótimo sem backtracking exaustivo.

---

## Como executar a Parte 2

É necessário ter o Python 3 instalado.

### Grafo pequeno

```bash
python3 parte2/coloracao_guloso.py parte2/grafo_wifi_p.txt parte2/saida_parte2_p.txt
```

### Grafo médio

```bash
python3 parte2/coloracao_dsatur.py parte2/grafo_wifi_m.txt parte2/saida_parte2_m.txt
```

---

## Saída esperada – grafo pequeno

Arquivo gerado: `parte2/saida_parte2_p.txt`

```txt
ALGORITMO: Guloso
JUSTIFICATIVA: O algoritmo guloso percorre os vertices em ordem e atribui a cada um a menor cor que nao conflite com seus vizinhos ja coloridos. E simples e eficiente, e produz resultado otimo para o grafo pequeno.
NUM_CORES: 3
COLORACAO: 0=1 1=2 2=3 3=1 4=2
```

---

## Saída esperada – grafo médio

Arquivo gerado: `parte2/saida_parte2_m.txt`

```txt
ALGORITMO: DSatur
JUSTIFICATIVA: DSatur escolhe a cada passo o vertice nao colorido com maior grau de saturacao (numero de cores distintas ja usadas pelos seus vizinhos), produzindo coloracoes proximas ao otimo sem necessidade de backtracking exaustivo.
NUM_CORES: 3
COLORACAO: 0=1 1=2 2=3 3=1 4=2 5=1 6=2 7=1
```

---

## Autoria

- Nelson Alves
- Francys Samuel
- Lucas Fernando
