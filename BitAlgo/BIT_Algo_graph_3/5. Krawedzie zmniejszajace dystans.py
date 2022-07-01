# Dany jest graf ważony z dodatnimi wagami G. Dana jest też lista E’ krawędzi, które nie należą do grafu,
# ale są krawędziami między wierzchołkami z G. Dane są również dwa wierzchołki s i t. Podaj algorytm, który stwierdzi,
# którą jedną krawędź z E’ należy wszczepić do G, aby jak najbardziej zmniejszyć dystans między s i t.
# Jeżeli żadna krawędź nie poprawi dystansu między s i t, to algorytm powinien to stwierdzić.


# Najpierw myślałem o stworzeniu grafu z wszystkimi krawędziami gdzie te z listy E będą oznaczone jako
# możliwe do użycia raz w trasie a te zwykłe dowolną ilość razy i na podstawie tego rozróżnienia
# uruchomić algorytm dijkstra a następnie w otrzymanym wyniku, tzn. trasie sprawdzić czy skorzystaliśmy
# z krawędzi z listy E, czyli oznaczonej jako do użycia raz. Jeśli tak zwracamy tą krawędź jeśli nie to None
# Problem: może powstać bardzo gęsty graf z paroma krawędziami między dwoma wierzchołkami, trzeba użyć jako
# reprezentacje grafu liste sąsiedztwa

# Zaimplementowany sposób liczy odległości algorytmem Dijsktra z wierzchołka s oraz z wierzchołka t
# (jeśli graf skierowany należy odwrócić krawędzie), a następnie z listy E, jeśli istnieje to znajduje
# krawędź która najbardziej skraca znaleziona wcześniej ścieżkę:

# Dijkstra s -> t ds[]
# Dla skierowanych: odwrócić krawędzie
# Dijkstra t -> s dt[]
# for u, v, w in E
#    ds[t] - (ds[u] + w + dt[v])


from math import inf
from queue import PriorityQueue


def decreasingEdges(G, E, s, t):
    n = len(G)
    ds = dijkstry(G, s)

    for i in range(n):
        for j in range(n):
            tmp = G[i][j]
            G[i][j] = G[j][i]
            G[j][i] = tmp

    dt = dijkstry(G, t)

    maxDiff = 0
    result = None
    for e in E:
        diff = ds[t] - (ds[e[0]] + e[2] + dt[e[1]])
        if diff > maxDiff:
            maxDiff = diff
            result = (e[0], e[1])

    return result


def dijkstry(G, s):
    n = len(G)
    dp = [inf for _ in range(n)]
    Q = PriorityQueue()

    dp[s] = 0
    Q.put((dp[s], s))

    while not Q.empty():
        _, u = Q.get()

        for i in range(n):
            if G[u][i] > 0 and dp[i] > dp[u] + G[u][i]:
                dp[i] = dp[u] + G[u][i]
                Q.put((dp[i], i))

    return dp
