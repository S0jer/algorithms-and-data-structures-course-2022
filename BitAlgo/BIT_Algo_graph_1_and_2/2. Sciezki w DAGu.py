# Ile możliwych ścieżek między s i t.


def pathsInDag(G, s, t):
    n = len(G)
    visited = [-1 for _ in range(n)]
    parents = [-1 for _ in range(n)]
    canTraverse = [False for _ in range(n)]
    canTraverse[t] = True

    paths = DFS(G, s, visited, parents, 0, t, canTraverse)

    return paths[0]


def DFS(G, u, visited, parents, paths, t, canTraverse):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if visited[i] != 1 and G[u][i] == 1:
            parents[i] = u
            paths, canTraverse, canTraverse[i] = DFS(G, i, visited, parents, paths, t, canTraverse)
            if canTraverse[i] is True:
                canTraverse[u] = True
        elif visited[i] == 1 and G[u][i] == 1 and canTraverse[i] is True:
            paths += 1

    if u == t or canTraverse[u] is True:
        canTraverse[u] = True
        return paths, canTraverse, True

    return paths, canTraverse, False


G = [[0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0]]

print(pathsInDag(G, 1, 8))
