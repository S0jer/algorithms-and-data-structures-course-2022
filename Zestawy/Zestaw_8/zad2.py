# Zadanie 2. (uniwersalne ujście) Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym ujściem,
# jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź wychodząca z t.
# 1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n2)).
# 2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.


def universalOut(graph):
    n = len(graph)
    visited = [-1 for _ in range(n)]
    topSorted = []

    for i in range(n):
        if visited[i] != 1:
            visited, topSorted = DFS(graph, visited, i, topSorted)

    return topSorted[::-1]


def DFS(G, visited, u, topSorted):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if visited[i] != 1 and G[u][i] == 1:
            DFS(G, visited, i, topSorted)

    topSorted.append(u)

    return visited, topSorted


graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

print(universalOut(graph))
