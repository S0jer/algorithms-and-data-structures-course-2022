# Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
# implementacji)


# Zmodyfikowana dijkstra licząca iloczyn nie sumę, bądź DFS/BFS również na podobnej zasadzie, np.
# BFS gdzie do kolejki po wartości trasy gdzie pierwszy wierzchołek v jaki wyciągniemy z kolejki
# zwróci nam również wartość minimalnej ścieżki z u do v


from math import inf
from queue import PriorityQueue


def BFSMinPathLog(G, s, k):
    n = len(G)
    Q = PriorityQueue()
    visited = [False for _ in range(n)]
    result = inf
    Q.put((1, s))

    while not Q.empty():
        rPrice, u = Q.get()
        visited[u] = True

        if u == k and result > rPrice:
            result = rPrice

        for i in range(n):
            if G[u][i] > 0 and visited[i] is False:
                Q.put((rPrice * G[u][i], i))

    return result


G = [[0, 2, 0, 0, 0, 4, 0, 0],
     [2, 0, 0, 9, 0, 0, 0, 0],
     [0, 0, 0, 5, 0, 0, 2, 1],
     [0, 9, 5, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 2, 0, 1],
     [4, 0, 0, 0, 2, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0]]

print(BFSMinPathLog(G, 1, 6))
