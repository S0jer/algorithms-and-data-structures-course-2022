# W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają mieszkańcy.
#
# struct Vertex {
#       bool shop; // true-sklep, false-dom
#       int* distances; // tablica odległości do innych wierzchołków
#       int* edges; // numery wierzchołków opisanych w distances
#       int edge; // rozmiar tablicy distances (i edges)
#       int d_store; // odległość do najbliższego sklepu
# };
#
# Zaimplementować funkcję distanceToClosestStore (int n, Vertex* village) uzupełniającą d_store dla tablicy Vertexów i oszacować złożoność algorytmu.


# Wrzucamy sklepy do kolejki i odpalamy Dijkstrę
# Lub tworzymy nowy graf gdzie mamy jedne super-sklep i dla niego uruchamiamyu Dijkstrę

from math import inf
from queue import PriorityQueue


def stores(G, S):
    n = len(G)
    dp = [inf for _ in range(n)]

    Q = PriorityQueue()
    for s in S:
        dp[s] = 0
        Q.put((dp[s], s))

    while not Q.empty():
        _, u = Q.get()

        for i in range(n):
            if G[u][i] > 0 and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                Q.put((dp[i], i))

    return dp


G = [[0, 4, 4, 6, 6, 0, 0, 0, 0, 2],
     [4, 0, 2, 0, 0, 0, 0, 0, 0, 0],
     [4, 2, 0, 8, 0, 2, 0, 0, 0, 0],
     [6, 0, 8, 0, 9, 0, 2, 0, 0, 0],
     [6, 0, 0, 9, 0, 0, 0, 0, 2, 0],
     [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

S = [1, 4]

print(stores(G, S))
