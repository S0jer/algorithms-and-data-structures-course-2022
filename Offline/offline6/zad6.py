# Paweł Jaśkowiec, 406165

# Algorytm polega na przejściu dwa razy BFSem raz z wierzchołka s, drugi raz z wierzchołka t.
# Otrzymamy z tego odległości wierzchołka s od reszty wierzchołków oraz analogicznie dla t,
# sumując wartości z obu tablic znajdujemy długość najkrótszej ścieżki oraz selekcjonujemy
# wierzchołki należące do potencjalnej najkrótszej ścieżki ( suma odległości od wierzchołka s i t dla danego wierzchołka
# musi być równa długości najkrótszej ścieżki )
# mając zbiór tych wierzchołków zliczamy wierzchołki kolejno odległe o 1, 2, 3 itd. od wierzchołka s,
# w przypadku otrzymania dla dwóch kolejnych odległości po jednym wierzchołku znajdujemy krawędź której usunięcie
# wydłuży najkrótszą ścieżkę


# Złożoność: V + E


from zad6testy import runtests
from collections import deque


def longer(G, s, t):
    n = len(G)
    roadFromS = BFS(G, s)
    roadFromT = BFS(G, t)
    minPathLength = roadFromS[0] + roadFromT[0]

    if roadFromS[t] == -1:
        return None

    dp = [[] for _ in range(minPathLength + 1)]

    for i in range(n):
        if roadFromS[i] + roadFromT[i] == minPathLength:
            dp[roadFromS[i]].append(i)

    # results = []
    for j in range(minPathLength):
        if len(dp[j]) == 1 and len(dp[j + 1]) == 1:
            return (dp[j][0], dp[j + 1][0])
            # results.append((dp[j][0], dp[j + 1][0]))

    # if len(results) > 0:
    #     return results[0]

    return None


def BFS(G, s):
    n = len(G)
    Q = deque()
    v = [-1] * n
    v_d = [-1] * n

    v_d[s] = 0
    v[s] = 1
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for i in G[u]:
            if v[i] != 1:
                v[i] = 1
                v_d[i] = v_d[u] + 1
                Q.append(i)

    return v_d


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
