import timeit
import numpy as np
from sys import maxsize
from itertools import permutations

def calcular_custo(caminho, matriz):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i+1]]
    custo += matriz[caminho[-1]][caminho[0]]  
    return custo

def forca_bruta(grafo, inicio):
    # Salvando os vértices
    vertices = []
    for vert in range(len(grafo)):
        if vert != inicio:
            vertices.append(vert)

    prox = permutations(vertices)
    caminhoAtual = maxsize

    # Fazendo o cálculo de custo
    for vert in prox:
        custoAtual = 0
        x = inicio

        for aresta in vert:
            custoAtual += float(grafo[x][aresta])
            x = aresta
        custoAtual += float(grafo[x][inicio])
        caminhoMin = min(caminhoAtual, custoAtual)

        if caminhoMin < caminhoAtual:
            caminhoAtual = min(caminhoAtual, custoAtual)
            aux = vert

    # Decidindo o melhor caminho
    melhorCaminho = []
    for vert in aux:
        melhorCaminho.append(vert)

    melhorCaminho.insert(0, inicio)
    melhorCaminho.append(inicio)

    return caminhoAtual, melhorCaminho

def gerar_matriz_aleatoria(): 
    matriz = np.random.randint(1, 100, size=(10, 10))
    np.fill_diagonal(matriz, 0)  # Garantir que a diagonal principal seja zero
    return matriz

def testar(matriz, nome_arquivo):   #aplica as funções nas matrizes
    inicio_total = timeit.default_timer()  
    custo_total_forca_bruta, _ = forca_bruta(matriz, 0)    
    fim_total = timeit.default_timer()  
    tempo_total = (fim_total - inicio_total)   

    print(f"Matriz Aleatória:")
    print(matriz)
    print(f"\nTestando a matriz: {nome_arquivo}")
    print(f"Tempo Total: {tempo_total:.3f} s")
    print(f"Custo Total Força Bruta: {custo_total_forca_bruta}")


matriz_aleatoria = gerar_matriz_aleatoria()

# Testar a matriz aleatória
print("\nTestando a matriz aleatória:")
testar(matriz_aleatoria, "matriz_aleatoria")
