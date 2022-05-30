from queue import Queue

from zad8testy import runtests


# Paweł Jaśkowiec, 406165

# Pomysł polega na wyznaczeniu minimalnego drzewa rozpinającego za pomocą algorytmu Kruskala podanego
# na wykładzie oraz następnie na podstawie otrzymanego drzewa zamianie niektórych krawędzi na bardziej
# optymalne względem warunków podanych w zadaniu w celu znalezienia rozwiązania


def highway(A):
    n = len(A)
    graph = [[-1 for _ in range(n)] for _ in range(n)]
    calculateLength(graph, A, n)
    edges = kruskal(graph)
    values = [graph[i][j] for i, j in edges]
    connected = [0 for _ in range(n)]
    miniGraph = [[0 for _ in range(n)] for _ in range(n)]

    for e in edges:
        connected[e[0]] += 1
        connected[e[1]] += 1
        miniGraph[e[0]][e[1]] = 1
        miniGraph[e[1]][e[0]] = 1

    for i in range(len(edges)):
        connected[edges[i][0]] -= 1
        connected[edges[i][1]] -= 1
        miniGraph[edges[i][0]][edges[i][1]] = 0
        miniGraph[edges[i][1]][edges[i][0]] = 0
        toConnect = (edges[i][0], edges[i][1])
        beforeChange = values[i]
        if connected[edges[i][0]] > 0 and connected[edges[i][1]] > 0:
            for k in range(2):
                diff = max(values) - min(values)
                for j in range(n):
                    toChange = values[i]
                    if graph[edges[i][k]][j] > 0 and (connected[j] > 0 or connected[edges[i][k]] > 0):
                        values[i] = graph[edges[i][k]][j]
                        if max(values) - min(values) < diff:
                            toConnect = (edges[i][k], j)
                            diff = max(values) - min(values)
                            beforeChange = toChange
                        else:
                            values[i] = toChange
        elif connected[edges[i][0]] == 0 and connected[edges[i][1]] == 0:
            connected[edges[i][0]] += 1
            connected[edges[i][1]] += 1
            miniGraph[edges[i][0]][edges[i][1]] = 1
            miniGraph[edges[i][1]][edges[i][0]] = 1
            break
        elif connected[edges[i][0]] == 0:
            diff = max(values) - min(values)
            for j in range(n):
                toChange = values[i]
                if graph[edges[i][0]][j] > 0 and connected[j] > 0:
                    values[i] = graph[edges[i][0]][j]
                    if max(values) - min(values) < diff:
                        toConnect = (edges[i][0], j)
                        diff = max(values) - min(values)
                        beforeChange = toChange
                    else:
                        values[i] = toChange
        elif connected[edges[i][1]] == 0:
            diff = max(values) - min(values)
            for j in range(n):
                toChange = values[i]
                if graph[edges[i][1]][j] > 0 and connected[j] > 0:
                    values[i] = graph[edges[i][1]][j]
                    if max(values) - min(values) < diff:
                        toConnect = (edges[i][1], j)
                        diff = max(values) - min(values)
                        beforeChange = toChange
                    else:
                        values[i] = toChange

        for c in toConnect:
            connected[c] += 1
        miniGraph[toConnect[0]][toConnect[1]] = 1
        miniGraph[toConnect[1]][toConnect[0]] = 1

        if not BFS(miniGraph, 0):
            for c in toConnect:
                connected[c] -= 1
            miniGraph[toConnect[0]][toConnect[1]] = 0
            miniGraph[toConnect[1]][toConnect[0]] = 0
            connected[edges[i][0]] += 1
            connected[edges[i][1]] += 1
            miniGraph[edges[i][0]][edges[i][1]] = 1
            miniGraph[edges[i][1]][edges[i][0]] = 1
            values[i] = beforeChange

    return max(values) - min(values)


def BFS(G, s):
    n = len(G)
    Q = Queue()
    v = [0] * n
    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        v[u] = 1
        for i in range(n):
            if v[i] != 1 and G[u][i] == 1:
                Q.put(i)

    return sum(v) == n


def kruskal(G):
    n = len(G)
    E, A = [], []

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                E.append(((i, j), G[i][j]))
    E.sort(key=lambda x: x[1])

    m = len(E)
    parents = [i for i in range(m)]
    rank = [0 for _ in range(m)]

    for i in range(m):
        if find(E[i][0][0], parents) != find(E[i][0][1], parents):
            union(E[i][0][0], E[i][0][1], parents, rank)
            A.append(E[i][0])

    return A


def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)

    return parents[x]


def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)

    if x == y:
        return

    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def calculateLength(graph, A, n):
    for i in range(n):
        for j in range(i, n):
            val = int(((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** (1 / 2))
            graph[i][j] = val
            graph[j][i] = val


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)
