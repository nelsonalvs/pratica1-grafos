import sys


def ler_grafo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8-sig") as arquivo:
        linhas = [linha.strip().split() for linha in arquivo if linha.strip()]

    num_vertices, num_arestas = map(int, linhas[0])

    adjacencia = [[] for _ in range(num_vertices)]

    for linha in linhas[1:]:
        u, v = map(int, linha)
        adjacencia[u].append(v)
        adjacencia[v].append(u)

    return num_vertices, adjacencia


def calcular_grau_saturacao(vertice, cores, adjacencia):
    # Retorna o numero de cores distintas ja usadas pelos vizinhos do vertice
    # TODO: implementar
    pass


def escolher_proximo_vertice(num_vertices, cores, adjacencia, graus):
    # Retorna o vertice nao colorido com maior grau de saturacao.
    # Em caso de empate, escolhe o de maior grau. Em novo empate, o de menor indice.
    # TODO: implementar
    pass


def encontrar_menor_cor_disponivel(vertice, cores, adjacencia):
    # Retorna a menor cor (inteiro >= 1) que nenhum vizinho do vertice usa
    # TODO: implementar
    pass


def dsatur(num_vertices, adjacencia):
    # Aplica o algoritmo DSatur e retorna uma lista onde cores[v] e a cor do vertice v
    # TODO: implementar usando as funcoes acima
    pass


def resolver(caminho_entrada, caminho_saida):
    num_vertices, adjacencia = ler_grafo(caminho_entrada)

    cores = dsatur(num_vertices, adjacencia)

    num_cores = len(set(cores))

    coloracao = " ".join(str(v) + "=" + str(cores[v]) for v in range(num_vertices))

    algoritmo = "DSatur"
    justificativa = (
        "DSatur escolhe a cada passo o vertice nao colorido com maior grau de saturacao "
        "(numero de cores distintas ja usadas pelos seus vizinhos), produzindo coloracoes "
        "proximas ao otimo sem necessidade de backtracking exaustivo."
    )

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("ALGORITMO: " + algoritmo + "\n")
        arquivo.write("JUSTIFICATIVA: " + justificativa + "\n")
        arquivo.write("NUM_CORES: " + str(num_cores) + "\n")
        arquivo.write("COLORACAO: " + coloracao + "\n")


def main():
    if len(sys.argv) != 3:
        print("Uso: python coloracao_dsatur.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    resolver(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
