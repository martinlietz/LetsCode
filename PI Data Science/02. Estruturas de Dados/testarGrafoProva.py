import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def run():

    num_ligacoes = int(input("Quantas pessoas conectadas?"))
    print(num_ligacoes)

    g = nx.Graph()

    users = []
    connections = []
    for i in range(num_ligacoes):
        nomes = str(input("Digita os usuarios com conexao - use espaço para separar os nomes:"))
        print(nomes)
        connections.append(nomes.split())
        users.extend(nomes.split())
    users = list(set(users))
    print(users)
    print(connections)

    for u in users:
        g.add_node(u)
    for c in connections:
        g.add_edge(c[0], c[1])
    print("\n\nMatriz de adjacência:\n")

    m = nx.adjacency_matrix(g).todense()

    print(m)

    pesquise = str(input("Nome de uma pessoa:"))
    print(pesquise)

    # newlist = [x for x in g.neighbors(pesquise) ]
    newlist = [x for x in nx.single_source_shortest_path_length(g,pesquise) if x != pesquise ]
    print(newlist)


    nx.draw_networkx(g, node_color="blue")

run()