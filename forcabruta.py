import timeit
import numpy as np
from sys import maxsize
import sys

def calcular_custo(caminho, matriz):    # calcula o custo do caminho
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i+1]]
    custo += matriz[caminho[-1]][caminho[0]]  
    return custo

def forca_bruta(distances, n): #aplica a algoritmo de força bruta
    min_distance = maxsize
    min_path = []

    def tsp_helper(path, visited, current_node, remaining_nodes, total_distance): #carteiro viajante
        nonlocal min_distance, min_path

        if len(remaining_nodes) == 0:
            total_distance += distances[current_node][path[0]]
            if total_distance < min_distance:
                min_distance = total_distance
                min_path = path[:] + [path[0]]

        for node in remaining_nodes:
            if node not in visited:
                new_distance = total_distance + distances[current_node][node]
                if new_distance < min_distance:
                    visited.add(node)
                    tsp_helper(path + [node], visited, node, remaining_nodes - {node}, new_distance)
                    visited.remove(node)

    for i in range(n):
        tsp_helper([i], {i}, i, set(range(n)) - {i}, 0)

    return min_distance, min_path

def carregar_matriz_adj(nome_arquivo): #carrega os dados txt em formato de matriz de adjacência
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()


    linhas = [linha.strip() for linha in linhas if linha.strip()]

    num_vertices = len(linhas)
    matriz_adj = np.zeros((num_vertices, num_vertices), dtype=int)  

    for i, linha in enumerate(linhas):
        valores = linha.split()
        for j, valor in enumerate(valores):
            matriz_adj[i][j] = int(valor)  
    
    return matriz_adj

def testar(matriz, nome_arquivo):   #aplica as funções nas matrizes
    inicio_total = timeit.default_timer()  
    custo_total_forca_bruta, _ = forca_bruta(matriz, len(matriz))    
    fim_total = timeit.default_timer()  
    tempo_total = (fim_total - inicio_total)   
        
    print(f"Matriz: {nome_arquivo}")
    print(f"Tempo Total: {tempo_total:.3f} s")
    print(f"Custo Total Força Bruta: {custo_total_forca_bruta}")

# Carregar as matrizes
matriz_adj_att48 = carregar_matriz_adj('bases/att48_d.txt')
matriz_adj_dantzig42 = carregar_matriz_adj('bases/dantzig42_d.txt')
matriz_adj_fri26 = carregar_matriz_adj('bases/fri26_d.txt')
matriz_adj_gr17 = carregar_matriz_adj('bases/gr17_d.txt')
matriz_adj_p01 = carregar_matriz_adj('bases/p01_d.txt')

# Testar as matrizes
print("\nTestando as matrizes:")
testar(matriz_adj_att48, "att48")
testar(matriz_adj_dantzig42, "dantzig42")
testar(matriz_adj_fri26, "fri26")
testar(matriz_adj_gr17, "gr17")
testar(matriz_adj_p01, "p01")
