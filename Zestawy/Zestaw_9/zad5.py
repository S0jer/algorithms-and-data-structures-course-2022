# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów. Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów
# i musi ich podzielić na grupki tak, żeby każda grupka mogła przebyć trasę bez rodzielania się.
# Proszę podać algorytm, który oblicza na ile (najmniej) grupek przewodnik musi podzielić turystów
# (i jaką trasą powinni się poruszać), źeby wszyscy dostali się z A do B.


# Trochę Dijkstra tylko nie liczy minimalną wartość trasy tylko maksymalną wartość trasy którą wyznacza
# odcinek o minimalnej wartości na danej trasie :)


from queue import PriorityQueue

from math import inf, ceil


def guide(G, A, B, K):
    m, n = len(G), 0
    for i in range(m):
        n = max(n, G[i][0], G[i][1])
    n += 1
    graph = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        x, y, z = G[i]
        graph[x][y] = z
        graph[y][x] = z

    dp = [-inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    Q = PriorityQueue()
    dp[A] = inf
    Q.put(A)

    while not Q.empty():
        u = Q.get()

        for i in range(n):
            roadVal = min(graph[u][i], dp[u])
            if graph[u][i] > 0 and roadVal > dp[i]:
                parents[i] = u
                dp[i] = roadVal
                Q.put(i)

    result = ceil(K / dp[B])
    return result


G = [(0, 1, 15), (0, 2, 7), (0, 3, 12), (1, 5, 8), (5, 6, 9), (3, 5, 10), (3, 4, 11), (4, 6, 15), (2, 4, 9)]
print(guide(G, 0, 6, 30))
