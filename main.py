import networkx as nx
import numpy as np

def criar_grafo_e_matriz_adjacencia(arquivo):
    # Crie um grafo direcionado
    G = nx.DiGraph()

    # Leia o arquivo de texto e adicione as arestas ao grafo
    with open(arquivo, 'r') as file:
        for line in file:
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)

    # Gere a matriz de adjacência
    matriz_adj = nx.to_numpy_array(G, dtype=int)

    return G, matriz_adj

# Exemplo de uso:
nome_arquivo = "grafo.txt"
grafo, matriz = criar_grafo_e_matriz_adjacencia(nome_arquivo)
print("Matriz de Adjacência:")
print(matriz)

# Agora você pode fazer alterações no grafo, por exemplo:
grafo.add_edge(1, 3)
print("Novo Grafo:")
print(list(grafo.edges()))
