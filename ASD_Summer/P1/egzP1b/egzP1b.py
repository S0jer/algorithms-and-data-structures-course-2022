from egzP1btesty import runtests
from queue import PriorityQueue
from math import inf


# Dijkstra z warunkami adekwatnym do zadania, nie można wejść na start i na metę nie mając 3 atrakcji odwiedzonych,
# max 3 atrkacje odwiedzone itp

def turysta(G, D, L):
    m, n = len(G), 0

    for i in range(m):
        if G[i][0] > n:
            n = G[i][0]
        if G[i][1] > n:
            n = G[i][1]
    n += 1
    graph = [[] for _ in range(n)]

    for j in range(m):
        graph[G[j][0]].append([G[j][1], G[j][2]])
        graph[G[j][1]].append([G[j][0], G[j][2]])

    Q = PriorityQueue()
    dp = [inf for _ in range(n)]
    dp[D] = 0
    Q.put((dp[D], D, 0, -1))

    while not Q.empty():
        roadP, u, pT, last = Q.get()

        for e in graph[u]:
            if e[0] == L and pT == 3 and dp[L] > roadP + e[1]:
                dp[L] = roadP + e[1]
            elif pT + 1 <= 3 and e[0] != D and e[0] != L and e[0] != last:
                Q.put((roadP + e[1], e[0], pT + 1, u))
        if dp[L] != inf:
            return dp[L]

    return dp[L]


runtests(turysta)
