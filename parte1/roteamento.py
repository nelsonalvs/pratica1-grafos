import sys
import math
import heapq


def ler_grafo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8-sig") as arquivo:
        linhas = [linha.strip().split() for linha in arquivo if linha.strip()]

    num_vertices, num_arestas = map(int, linhas[0])
    origem, destino = map(int, linhas[1])

    arestas = []
    adjacencia = [[] for _ in range(num_vertices)]

    for linha in linhas[2:]:
        u, v, peso = map(int, linha)
        arestas.append((u, v, peso))
        adjacencia[u].append((v, peso))

    return num_vertices, origem, destino, arestas, adjacencia


def possui_peso_negativo(arestas):
    return any(peso < 0 for _, _, peso in arestas)


def reconstruir_caminho(origem, destino, anterior):
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)

        if atual == origem:
            break

        atual = anterior[atual]

    caminho.reverse()

    if not caminho or caminho[0] != origem:
        return []

    return caminho


def dijkstra(num_vertices, origem, destino, adjacencia):
    dist = [math.inf] * num_vertices
    anterior = [None] * num_vertices

    dist[origem] = 0
    fila = [(0, origem)]

    while fila:
        custo_atual, u = heapq.heappop(fila)

        if custo_atual > dist[u]:
            continue

        for v, peso in adjacencia[u]:
            novo_custo = dist[u] + peso

            if novo_custo < dist[v]:
                dist[v] = novo_custo
                anterior[v] = u
                heapq.heappush(fila, (novo_custo, v))

    rota = reconstruir_caminho(origem, destino, anterior)
    return dist[destino], rota


def bellman_ford(num_vertices, origem, destino, arestas):
    dist = [math.inf] * num_vertices
    anterior = [None] * num_vertices

    dist[origem] = 0

    for _ in range(num_vertices - 1):
        atualizou = False

        for u, v, peso in arestas:
            if dist[u] != math.inf and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                anterior[v] = u
                atualizou = True

        if not atualizou:
            break

    for u, v, peso in arestas:
        if dist[u] != math.inf and dist[u] + peso < dist[v]:
            raise ValueError("O grafo possui ciclo negativo alcancavel pela origem.")

    rota = reconstruir_caminho(origem, destino, anterior)
    return dist[destino], rota


def resolver(caminho_entrada, caminho_saida):
    num_vertices, origem, destino, arestas, adjacencia = ler_grafo(caminho_entrada)

    if possui_peso_negativo(arestas):
        algoritmo = "Bellman-Ford"
        justificativa = (
            "O grafo contem arestas com peso negativo, o que invalida Dijkstra. "
            "Bellman-Ford suporta pesos negativos e ainda permite detectar ciclos negativos."
        )
        custo, rota = bellman_ford(num_vertices, origem, destino, arestas)
    else:
        algoritmo = "Dijkstra"
        justificativa = (
            "Todos os pesos das arestas sao nao negativos, portanto Dijkstra e aplicavel "
            "e encontra o menor caminho de forma eficiente."
        )
        custo, rota = dijkstra(num_vertices, origem, destino, adjacencia)

    with open(caminho_saida, "w", encoding="utf-8-sig") as arquivo:
        arquivo.write(f"ALGORITMO: {algoritmo}\n")
        arquivo.write(f"JUSTIFICATIVA: {justificativa}\n")
        arquivo.write("ROTA: " + " ".join(map(str, rota)) + "\n")
        arquivo.write(f"CUSTO: {custo:g}\n")


def main():
    if len(sys.argv) != 3:
        print("Uso: python roteamento.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    resolver(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
