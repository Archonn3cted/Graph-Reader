import numpy as np
from random import randint

#Implementação do algoritmo de Prim para encontrar AGM
def minimal_spanning_tree(graph, mode='Prim', starting_node=None):
    if mode == 'Prim':
        return _minimal_spanning_tree_prim(graph, starting_node)

def _minimal_spanning_tree_prim(graph, starting_node):
    node_count = len(graph)
    all_nodes = [i for i in range(node_count)]
    if starting_node is None:
        starting_node = randint(0, node_count-1)
    unvisited_nodes = all_nodes
    visited_nodes = [starting_node]
    unvisited_nodes.remove(starting_node)
    mst = np.zeros((node_count, node_count))
    while len(visited_nodes) != node_count:
        selected_subgraph = graph[np.array(visited_nodes)[:, None], np.array(unvisited_nodes)]
        #Esta linha encontra o índice da aresta de peso mínimo no subgrafo selecionado.
        min_edge_index = np.unravel_index(np.ma.masked_equal(selected_subgraph, 0, copy=False).argmin(),
                                          selected_subgraph.shape)
        edge_from = visited_nodes[min_edge_index[0]]
        edge_to = unvisited_nodes[min_edge_index[1]]
        mst[edge_from, edge_to] = graph[edge_from, edge_to]
        mst[edge_to, edge_from] = graph[edge_from, edge_to]
        unvisited_nodes.remove(edge_to)
        visited_nodes.append(edge_to)
    return mst

#Esta função calcula o custo total de percorrer o caminho
def route_cost(graph, path):
    cost = 0
    for index in range(len(path) - 1):
        cost = cost + graph[path[index]][path[index + 1]]
    # adiciona o custo da última aresta do caminho para formar um ciclo completo.
    cost = cost + graph[path[-1], path[0]]
    return cost