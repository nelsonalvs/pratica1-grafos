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


def encontrar_menor_cor_disponivel(vertice, cores, adjacencia):
    cores_dos_vizinhos = set()

    for vizinho in adjacencia[vertice]:
        if cores[vizinho] != 0:
            cores_dos_vizinhos.add(cores[vizinho])

    cor = 1
    while cor in cores_dos_vizinhos:
        cor += 1

    return cor


def coloracao_gulosa(num_vertices, adjacencia):
    cores = [0] * num_vertices

    for v in range(num_vertices):
        cores[v] = encontrar_menor_cor_disponivel(v, cores, adjacencia)

    return cores


def resolver(caminho_entrada, caminho_saida):
    num_vertices, adjacencia = ler_grafo(caminho_entrada)

    cores = coloracao_gulosa(num_vertices, adjacencia)

    num_cores = len(set(cores))

    coloracao = " ".join(str(v) + "=" + str(cores[v]) for v in range(num_vertices))

    algoritmo = "Guloso"
    justificativa = (
        "O algoritmo guloso percorre os vertices em ordem e atribui a cada um a menor cor "
        "que nao conflite com seus vizinhos ja coloridos. E simples e eficiente, "
        "e produz resultado otimo para o grafo pequeno."
    )

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("ALGORITMO: " + algoritmo + "\n")
        arquivo.write("JUSTIFICATIVA: " + justificativa + "\n")
        arquivo.write("NUM_CORES: " + str(num_cores) + "\n")
        arquivo.write("COLORACAO: " + coloracao + "\n")


def main():
    if len(sys.argv) != 3:
        print("Uso: python coloracao_guloso.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    resolver(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
