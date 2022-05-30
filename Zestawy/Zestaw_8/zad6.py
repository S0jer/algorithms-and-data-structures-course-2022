# Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
# nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
# korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
# Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
# metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
# z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
# Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.


from collections import deque


def safeFlightBFS(G, height, t, s, meta):
    n = len(G)
    visited = [False for _ in range(n)]
    Q = deque()

    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        visited[u] = True
        for station in G[u]:
            if visited[station[0]] is False and height - t <= station[1] <= height + t:
                Q.append(station[0])

    return visited[meta]


def safeFlightDFS(G, visited, u, height, t, meta):
    visited[u] = 1

    for station in G[u]:
        if visited[station[0]] != 1 and height - t <= station[1] <= height + t:
            safeFlightDFS(G, visited, station[0], height, t, meta)

    if visited[meta] == 1:
        return True
    return False


graph = [[(1, 15), (3, 11), (2, 12)],
         [(5, 14), (0, 15), (4, 11)],
         [(4, 10), (0, 12)],
         [(6, 15), (0, 11)],
         [(1, 11), (7, 17), (2, 10)],
         [(6, 13), (7, 18), (1, 14)],
         [(7, 14), (3, 15), (5, 13)],
         [(4, 17), (5, 18), (6, 10)]]

s, k, p, t = 0, 7, 12, 2

print(safeFlightDFS(graph, [-1 for _ in range(len(graph))], s, p, t, k))
print(safeFlightBFS(graph, p, t, s, k))
