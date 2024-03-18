class Grafo:

    def __init__(self, numeroVertices):
        self.numeroVertices = numeroVertices
        self.matrizAdjacencia = [[0] * numeroVertices for _ in range(numeroVertices)]

    def adicionarAresta(self, vertice_1, vertice_2, peso):
        self.matrizAdjacencia[vertice_1][vertice_2] = peso

    def dijkstra(self, origem):
        distancia = [float('inf')] * self.numeroVertices
        distancia[origem] = 0
        verticesVisitados = [False] * self.numeroVertices

        for _ in range(self.numeroVertices):
            u = self.minDistancia(distancia, verticesVisitados)
            verticesVisitados[u] = True

            for v in range(self.numeroVertices):
                if (self.matrizAdjacencia[u][v] > 0 and not verticesVisitados[v] and
                        distancia[v] > distancia[u] + self.matrizAdjacencia[u][v]):
                    distancia[v] = distancia[u] + self.matrizAdjacencia[u][v]

        self.imprimirCaminhos(origem, distancia)

    def minDistancia(self, distancia, verticesVisitados):
        minDist = float('inf')
        minIndex = -1

        for v in range(self.numeroVertices):
            if distancia[v] < minDist and not verticesVisitados[v]:
                minDist = distancia[v]
                minIndex = v

        return minIndex

    def imprimirCaminhos(self, origem, distancia):
        print("Caminhos mínimos a partir do vértice:", origem)
        for i in range(self.numeroVertices):
            print("Vértice:", i, "Distância:", distancia[i])