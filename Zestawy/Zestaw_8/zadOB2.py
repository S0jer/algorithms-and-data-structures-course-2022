# Zadanie 2. (cykl na cztery) Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
# algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy,
# że graf reprezentowany jest przez macierz sasiedztwa A.


def findCycle(G, k):
    n = len(G)
    result = []
    i = 0

    while i < n:
        visited = [-1 for _ in range(n)]
        cycle = DFS(G, visited, i, [i], k, i)
        if len(cycle) == k + 1:
            result = cycle
        i += 1

    return result


def DFS(G, visited, u, cycle, k, start):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if len(cycle) == 1 and k - 1 > 0 and visited[i] != 1 and G[u][i] == 1:
            DFS(G, visited, i, cycle, k - 1, start)

    if (k - 1 == 0 and G[u][start] == 1) or k - 1 > 0:
        cycle.append(u)
        return cycle
    else:
        return cycle


G = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]

G3 = [[0, 1, 1, 1, 1],
      [1, 0, 1, 1, 1],
      [1, 1, 0, 0, 1],
      [1, 1, 0, 0, 1],
      [1, 1, 1, 1, 0]]

print(findCycle(G, 4))
print()
print(findCycle(G3, 4))
