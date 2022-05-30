# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek.



def goodStart(G):
    n = len(G)

    for i in range(n):
        sorTp, visited = DFSTP(G, [0] * n, i, [])

        if sum(visited) == n:
            return True

    return False


def DFSTP(G, visited, u, sorTp):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if G[u][i] > 0 and visited[i] == 0:
            DFSTP(G, visited, i, sorTp)

    sorTp.append(u)

    return sorTp, visited


adj = [[0, 1, 1, 1, 0],
       [1, 0, 1, 0, 1],
       [1, 1, 0, 1, 1],
       [1, 0, 1, 0, 0]]

G = [[0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 1, 0, 0]]

print(goodStart(adj))
print(goodStart(G))
