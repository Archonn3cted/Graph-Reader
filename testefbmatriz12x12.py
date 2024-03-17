import timeit
import numpy as np
import itertools

def calcular_custo(caminho, matriz):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += matriz[caminho[i]][caminho[i+1]]
    custo += matriz[caminho[-1]][caminho[0]]  # Adiciona o custo de retorno para a cidade inicial
    return custo

def forca_bruta(matriz):
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
    matriz = np.random.randint(1, 100, size=(12, 12))
    np.fill_diagonal(matriz, 0)  # Garantir que a diagonal principal seja zero
    return matriz

def testar(matriz, repetir):
    with open("matriz_12x12_resultados.txt", "w") as arquivo_resultado:
        for i in range(repetir):
            inicio = timeit.default_timer()  # Inicia o temporizador
            custo, menor_caminho = forca_bruta(matriz)
            fim = timeit.default_timer()  # Finaliza o temporizador
            tempo_total_segundos = fim - inicio  # Calcula o tempo total em segundos
            tempo_total_minutos = tempo_total_segundos / 60  # Converte o tempo total para minutos
            arquivo_resultado.write(f"Tempo Total: {tempo_total_minutos:.3f} minutos\n")
            arquivo_resultado.write(f"Custo: {custo}\n")
            #arquivo_resultado.write(f"Caminho: {menor_caminho}\n")

# Gerar uma matriz grande
matriz_grande = gerar_matriz_grande()

# Apresentar a matriz grande
print("Matriz Grande:")
print(matriz_grande)

# Testar a matriz grande
print("\nTestando a matriz grande:")
testar(matriz_grande, 1)
