# Zadanie 2. (domknięcie przechodnie) Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu
# reprezentowanego w postaci macierzowej (domknięcie przechodnie grafu G, to graf nad tym samym zbiorem wierzchołków,
# który dla każdych dwóch wierzchołków u i v ma krawędź z u do v wtedy i tylko wtedy, gdy w G istnieje ścieżka z u do v.


from math import inf


# Czyli Floyd-Warchall


def domkniecie(G):
    n = len(G)
    graph = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            graph[i][j] = G[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + G[k][i])

    return graph

