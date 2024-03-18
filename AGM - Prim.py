import os
import time
import numpy as np
import tsplib95

def AGM_Prim(matrizAdj):
    numVertices = len(matrizAdj)
    visitados = [False] * numVertices
    pesos = [float('inf')] * numVertices
    pesos[0] = 0
    pai = [-1] * numVertices

    tempoInicio = time.time()

    for _ in range(numVertices):
        u = encontrarVerticeMenorPeso(visitados, pesos)
        visitados[u] = True

        for v in range(numVertices):
            if matrizAdj[u][v] > 0 and not visitados[v] and matrizAdj[u][v] < pesos[v]:
                pai[v] = u
                pesos[v] = matrizAdj[u][v]

    tempoFim = time.time()
    tempoExecucao = tempoFim - tempoInicio

    return pai, tempoExecucao

def encontrarVerticeMenorPeso(visitados, pesos):
    minPeso = float('inf')
    minVertice = -1

    for v, peso in enumerate(pesos):
        if not visitados[v] and peso < minPeso:
            minPeso = peso
            minVertice = v

    return minVertice

def carregarMatrizAdjacencia(nomeArquivo):
    problema = tsplib95.load(nomeArquivo)
    edgeWeightType = problema.edge_weight_type
    formatoPesoAresta = problema.edge_weight_format

    if edgeWeightType == 'EXPLICIT' and formatoPesoAresta == 'FULL_MATRIX':
        return np.array(problema.edge_weights)

    elif edgeWeightType == 'EXPLICIT' and formatoPesoAresta == 'LOWER_DIAG_ROW':
        matriz = np.zeros((problema.dimension, problema.dimension), dtype=int)
        pesosArestas = problema.edge_weights
        pesosArestasFlat = [peso for sublist in pesosArestas for peso in sublist]
        pesoIndex = 0
        for i in range(problema.dimension):
            for j in range(i + 1):
                matriz[i][j] = pesosArestasFlat[pesoIndex]
                pesoIndex += 1
        for i in range(problema.dimension):
            for j in range(i + 1, problema.dimension):
                matriz[i][j] = matriz[j][i]
        return matriz

    elif edgeWeightType == 'ATT':
        matriz = np.zeros((problema.dimension, problema.dimension), dtype=int)
        coordenadas = problema.node_coords
        for i in range(problema.dimension):
            for j in range(problema.dimension):
                xi, yi = coordenadas[i+1]
                xj, yj = coordenadas[j+1]
                distancia = int(round(np.sqrt((xi - xj)**2 + (yi - yj)**2)))
                matriz[i][j] = distancia
        return matriz

    else:
        raise ValueError("Formato de peso de aresta não suportado.")

def calcularLimiteInferior(nomeArquivo):
    matrizAdj = carregarMatrizAdjacencia(nomeArquivo)
    pai, tempoExecucao = AGM_Prim(matrizAdj)
    pesoAGM = sum([matrizAdj[i][pai[i]] for i in range(1, len(pai))])
    custoRetorno = matrizAdj[pai[-1]][0]
    limiteInferior = pesoAGM + custoRetorno
    return limiteInferior, pesoAGM, tempoExecucao

#Para testar os arquivos, deixa com "#" as variável "arquivo_tsp" que não pretende usar e deixa sem a variável que pretende usar
#arquivoTSP = "bases/att48.tsp"
#arquivoTSP = "bases/dantzig42.tsp"
#arquivoTSP = "bases/fri26.tsp"
#arquivoTSP = "bases/gr17.tsp"
arquivoTSP = "bases/p01.tsp"

# Extrair o nome do arquivo sem o caminho
nomeBase = os.path.basename(arquivoTSP)

limiteInferior, pesoAGM, tempoExecucao = calcularLimiteInferior(arquivoTSP)
print("Base:", nomeBase)
print("Limite Inferior para o TSP:", int(limiteInferior))
print("Custo da AGM:", int(pesoAGM))
print("Tempo de Execução do algoritmo de Prim:", format(tempoExecucao, '.9f'), "segundos")
