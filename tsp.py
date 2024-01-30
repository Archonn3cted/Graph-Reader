import tsplib95

def grafo_att():
    problema = tsplib95.load('bases/att48.tsp')
    grafo1 = problema.get_graph()

    print(f'Nome: {problema.name}')    
    print(f'Tipo: {problema.type}')
    print(f'Dimensão: {problema.dimension}')
    print(f'Verices: {grafo1.nodes(data=True)}')
    print(f'Arestas: {grafo1.edges(data=True)}')

def grafo_dant():
    problema = tsplib95.load('bases/dantzig42.tsp')
    grafo2 = problema.get_graph()

    print(f'Nome: {problema.name}')
    print(f'Tipo: {problema.type}')
    print(f'Dimensão: {problema.dimension}')
    print(f'Verices: {grafo2.nodes(data=True)}')
    print(f'Arestas: {grafo2.edges(data=True)}')

def grafo_fri():
    problema = tsplib95.load('bases/fri26.tsp')
    grafo3 = problema.get_graph()

    print(f'Nome: {problema.name}')
    print(f'Tipo: {problema.type}')
    print(f'Dimensão: {problema.dimension}')
    print(f'Verices: {grafo3.nodes(data=True)}')
    print(f'Arestas: {grafo3.edges(data=True)}')

def grafo_gr17():
    problema = tsplib95.load('bases/gr17.tsp')
    grafo4 = problema.get_graph()

    print(f'Nome: {problema.name}')
    print(f'Tipo: {problema.type}')
    print(f'Dimensão: {problema.dimension}')
    print(f'Verices: {grafo4.nodes(data=True)}')
    print(f'Arestas: {grafo4.edges(data=True)}')

def grafo_p01():
    problema = tsplib95.load('bases/p01.tsp')
    grafo5 = problema.get_graph()

    print(f'Nome: {problema.name}')
    print(f'Tipo: {problema.type}')
    print(f'Dimensão: {problema.dimension}')
    print(f'Verices: {grafo5.nodes(data=True)}')
    print(f'Arestas: {grafo5.edges(data=True)}')