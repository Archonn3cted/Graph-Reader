import itertools
import numpy as np
import networkx as nx
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit
from arvoreGeradoraMinima import minimal_spanning_tree

def christofides_tsp(graph, starting_node=0):
    mst = minimal_spanning_tree(graph, 'Prim', starting_node=0)
    odd_degree_nodes = list(_get_odd_degree_vertices(mst))
    odd_degree_nodes_ix = np.ix_(odd_degree_nodes, odd_degree_nodes)
    nx_graph = nx.from_numpy_array(-1 * graph[odd_degree_nodes_ix])
    matching = max_weight_matching(nx_graph, maxcardinality=True)
    euler_multigraph = nx.MultiGraph(mst)
    for edge in matching:
        euler_multigraph.add_edge(odd_degree_nodes[edge[0]], odd_degree_nodes[edge[1]],
                                  weight=graph[odd_degree_nodes[edge[0]]][odd_degree_nodes[edge[1]]])
    euler_tour = list(eulerian_circuit(euler_multigraph, source=starting_node))
    path = list(itertools.chain.from_iterable(euler_tour))
    return _remove_repeated_vertices(path, starting_node)[:-1]

def _get_odd_degree_vertices(graph):
    odd_degree_vertices = set()
    for index, row in enumerate(graph):
        if len(np.nonzero(row)[0]) % 2 != 0:
            odd_degree_vertices.add(index)
    return odd_degree_vertices

def _remove_repeated_vertices(path, starting_node):
    path = list(dict.fromkeys(path).keys())
    path.append(starting_node)
    return path

def tour_cost(adj_matrix, tour):
    cost = 0
    for i in range(len(tour)):
        u = tour[i]
        v = tour[(i + 1) % len(tour)]
        cost += adj_matrix[u][v]
    return cost

def escolhaBaseDeDados():
    # Realiza a escolha da base de dados
    print("-=="*20)
    print('Escolha a base de dados desejada:')
    print('A - att48')
    print('B - dantzig42')
    print('C - fri26')
    print('D - gr17')
    print('E - p01')
    print("-=="*20)
    escolha = str(input('Digite a letra da respectiva base de dados que deseja analisar: ')).strip().upper()
    if escolha == 'A':
        basedeDados = "C:/Users/Rangell/OneDrive/Documentos/christofidesAlgoritm/Bases/att48_d.txt"
        return basedeDados
    if escolha == 'B':
        basedeDados = "C:/Users/Rangell/OneDrive/Documentos/christofidesAlgoritm/Bases/dantzig42_d.txt"
        return basedeDados
    if escolha == 'C':
        basedeDados = "C:/Users/Rangell/OneDrive/Documentos/christofidesAlgoritm/Bases/fri26_d.txt"
        return basedeDados
    if escolha == 'D':
        basedeDados = "C:/Users/Rangell/OneDrive/Documentos/christofidesAlgoritm/Bases/gr17_d.txt"
        return basedeDados
    if escolha == 'E':
        basedeDados = "C:/Users/Rangell/OneDrive/Documentos/christofidesAlgoritm/Bases/p01_d.txt"
        return basedeDados
    else:
        print('-=='*10)
        print('Opção inválida.')
        print('-=='*10)
        return escolhaBaseDeDados()

def lerArquivoTsp(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    # Inicializa a variável dados
    dados = []
    indiceSecao=0
    # Processar as linhas de pesos de arestas ou coordenadas
    numCidades = len(linhas) - indiceSecao
    # Inicializa a variável matrixDistancias
    matrixDistancias = []
    for i in range(indiceSecao, indiceSecao + numCidades):
        linhaStriped = linhas[i].strip()
        distancias = list(map(float, linhaStriped.split()))
        matrixDistancias.append(distancias)
    dados = matrixDistancias
    return dados

def main():
    # Caminho do arquivo a ser lido
    basedeDados = escolhaBaseDeDados()
    caminhoArquivo = basedeDados
    # Chama a função para ler os dados (pesos de arestas)
    dados = lerArquivoTsp(caminhoArquivo)
    # Exibe os dados
    graph = np.array(dados)
    print(graph)
    print(christofides_tsp(graph))
    print("Custo mínimo do tour:", tour_cost(graph, christofides_tsp(graph)))

if __name__ == "__main__":
    main()