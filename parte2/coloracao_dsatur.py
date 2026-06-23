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
    cores_vizinhos = set()
    for vizinho in adjacencia[vertice]:
        if cores[vizinho] != 0:
            cores_vizinhos.add(cores[vizinho])
    return len(cores_vizinhos)

def escolher_proximo_vertice(num_vertices, cores, adjacencia, graus):
    # Retorna o vertice nao colorido com maior grau de saturacao.
    # Em caso de empate, escolhe o de maior grau. Em novo empate, o de menor indice.
    melhor_vertice = -1
    max_sat = -1
    max_grau = -1

    for v in range(num_vertices):
        if cores[v] == 0:
            sat = calcular_grau_saturacao(v, cores, adjacencia)
            if sat > max_sat:
                max_sat = sat
                max_grau = graus[v]
                melhor_vertice = v
            elif sat == max_sat:
                if graus[v] > max_grau:
                    max_grau = graus[v]
                    melhor_vertice = v
    return melhor_vertice

def encontrar_menor_cor_disponivel(vertice, cores, adjacencia):
    # Retorna a menor cor (inteiro >= 1) que nenhum vizinho do vertice usa
    cores_dos_vizinhos = set()
    for vizinho in adjacencia[vertice]:
        if cores[vizinho] != 0:
            cores_dos_vizinhos.add(cores[vizinho])

    cor = 1
    while cor in cores_dos_vizinhos:
        cor += 1

    return cor

def dsatur(num_vertices, adjacencia):
    # Aplica o algoritmo DSatur e retorna uma lista onde cores[v] e a cor do vertice v
    graus = [len(adjacencia[v]) for v in range(num_vertices)]
    
    cores_iniciais = [0] * num_vertices
    for _ in range(num_vertices):
        u = escolher_proximo_vertice(num_vertices, cores_iniciais, adjacencia, graus)
        cor = encontrar_menor_cor_disponivel(u, cores_iniciais, adjacencia)
        cores_iniciais[u] = cor
        
    melhor_num_cores = len(set(cores_iniciais))
    melhor_solucao = cores_iniciais.copy()

    if melhor_num_cores <= 2:
        return melhor_solucao

    cores_backtracking = [0] * num_vertices

    def backtracking(vertices_coloridos):
        nonlocal melhor_num_cores, melhor_solucao

        if vertices_coloridos == num_vertices:
            num_cores_atual = len(set(cores_backtracking))
            if num_cores_atual < melhor_num_cores:
                melhor_num_cores = num_cores_atual
                melhor_solucao = cores_backtracking.copy()
            return

        u = escolher_proximo_vertice(num_vertices, cores_backtracking, adjacencia, graus)
        if u == -1:
            return

        cores_vizinhos = set(cores_backtracking[v] for v in adjacencia[u] if cores_backtracking[v] != 0)

        for cor in range(1, melhor_num_cores):
            if cor not in cores_vizinhos:
                cores_backtracking[u] = cor
                
                if len(set(cores_backtracking)) - (1 if 0 in cores_backtracking else 0) < melhor_num_cores:
                    backtracking(vertices_coloridos + 1)
                
                cores_backtracking[u] = 0

    backtracking(0)
    return melhor_solucao

def resolver(caminho_entrada, caminho_saida):
    num_vertices, adjacencia = ler_grafo(caminho_entrada)

    cores = dsatur(num_vertices, adjacencia)

    num_cores = len(set(cores))

    coloracao = " ".join(str(v) + "=" + str(cores[v]) for v in range(num_vertices))

    algoritmo = "DSatur com Backtracking Otimizado"
    justificativa = (
        "Utiliza DSatur como heuristica de ordenacao e limitante superior para um "
        "algoritmo de backtracking com poda. Garante a coloracao minima absoluta "
        "executando de forma eficiente mesmo em instancias maiores."
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