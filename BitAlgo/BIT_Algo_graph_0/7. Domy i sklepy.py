# Mamy mapę miasteczka, w którym są domy i sklepy. Na mapie są również drogi (każda długości 1), które łączą dom z domem,
# albo dom ze sklepem. Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu.

# Oznaczamy wszystkie sklepy jako odwiedzone i wstawiamy je do kolejki z odległością 0. Uruchamiamy BFSa z taką kolejką,
# zwiększając o 1 odległość przy dodawaniu nieodwiedzonych domów.

# Lub jeden super-sklep i z niego BFS

from queue import PriorityQueue
from math import inf


def houseAndShop(G, S):
    n = len(G)
    Q = PriorityQueue()
    dp = [inf for _ in range(n)]

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
