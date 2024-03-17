import timeit
import numpy as np
import itertools

def calcular_custo(caminho, matriz):
    """
    Calcula o custo total de um caminho na matriz de distâncias.

    Args:
        caminho (tuple): Uma tupla representando o caminho percorrido.
        matriz (np.ndarray): Matriz de distâncias entre cidades.

    Returns:
        float: O custo total do caminho.
    """
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i+1]]
    custo += matriz[caminho[-1]][caminho[0]]  # Adiciona o custo de retorno para a cidade inicial
    return custo

def forca_bruta(matriz):
    """
    Implementa o algoritmo de força bruta para resolver o problema do caixeiro viajante.

    Args:
        matriz (np.ndarray): Matriz de distâncias entre cidades.

    Returns:
        tuple: Uma tupla contendo o menor custo encontrado e o menor caminho.
    """
    menor_custo = float('inf')
    menor_caminho = None
    num_vertices = len(matriz)

    for permutacao in itertools.permutations(range(num_vertices)):  
        permutacao = permutacao + (permutacao[0],)  # Garantir que a permutação comece e termine no vértice inicial
        custo_atual = calcular_custo(permutacao, matriz)
        if custo_atual < menor_custo:
            menor_custo = custo_atual
            menor_caminho = permutacao

    return menor_custo, menor_caminho

def gerar_matriz_grande():
    """
    Gera uma matriz de distâncias aleatória de tamanho 10x10.

    Returns:
        np.ndarray: Matriz de distâncias entre cidades.
    """
    matriz = np.random.randint(1, 100, size=(10, 10))
    np.fill_diagonal(matriz, 0)  # Garantir que a diagonal principal seja zero
    return matriz

def testar(matriz, repetir):
    """
    Testa o algoritmo de força bruta em uma matriz de distâncias.

    Args:
        matriz (np.ndarray): Matriz de distâncias entre cidades.
        repetir (int): Número de repetições do teste.
    """
    for i in range(repetir):
        inicio = timeit.default_timer()  # Inicia o temporizador
        custo, menor_caminho = forca_bruta(matriz)
        fim = timeit.default_timer()  # Finaliza o temporizador
        tempo_total_segundos = fim - inicio  # Calcula o tempo total em segundos
        tempo_total_minutos = tempo_total_segundos / 60  # Converte o tempo total para minutos
        print(f"Iteração {i+1}:")
        print(f"Tempo Total: {tempo_total_minutos:.3f} minutos")
        print(f"Custo: {custo}")
        #print(f"Caminho: {menor_caminho}")

# Gerar uma matriz grande
matriz_grande = gerar_matriz_grande()

# Apresentar a matriz grande
print("Matriz Grande:")
print(matriz_grande)

# Testar a matriz grande
print("\nTestando a matriz grande:")
testar(matriz_grande, 1)
