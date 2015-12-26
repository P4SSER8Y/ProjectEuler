#coding:utf8
from os import path
import networkx as nx
import matplotlib.pyplot as plt

def pr082():
    f = open(path.split(path.realpath(__file__))[0] + '\\data082.txt', 'r')
    data = []
    for x in f.readlines():
        data.append(list(map(int, x.split(','))))
    f.close() 
    N = len(data)
    getNode = lambda i, j: i * N + j

    G = nx.Graph()
    for i in range(N):
        for j in range(N):
            if i > 0:
                G.add_edge(getNode(i, j), getNode(i-1, j), weight = (data[i-1][j] + data[i][j]) / 2)
            if i < N - 1:
                G.add_edge(getNode(i, j), getNode(i+1, j), weight = (data[i+1][j] + data[i][j]) / 2)
            if j < N - 1:
                G.add_edge(getNode(i, j), getNode(i, j+1), weight = (data[i][j+1] + data[i][j]) / 2)
    for i in range(N):
        G.add_edge('s', getNode(i, 0), weight = data[i][0] / 2)
        G.add_edge(getNode(i, N-1), 't', weight = data[i][N-1] / 2)

    return int(nx.shortest_path_length(G, source='s', target='t', weight = 'weight'))


def run():
    return pr082()

if __name__ == "__main__":
    print(run())
