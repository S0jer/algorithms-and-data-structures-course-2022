# W Krakowie w godzinach szczytu są korki, dlatego kierowcom bardziej zależy na czasie niż na realnej odległości
# między dwoma punktami. Mamy mapę Krakowa, między skrzyżowaniami na ulicach są zaznaczone odległości i czasy przejazdu.
# W Krakowie (jak wszyscy wiemy ;) ) są ulice jedno- i dwukierunkowe. Kierowcy potrzebują aplikacji, która pomoże
# im znajdować drogi, które pozwalają dotrzeć ze skrzyżowania A do B w jak najkrótszym czasie, a spośród tych o najmniejszym
# czasie wybiera i zwraca najkrótszą pod względem odległości.
# Mamy przetworzyć Q zapytań w postaci (skrzyżowanieA, skrzyżowanieB) i na każde z nich odpowiedzieć parą (czas, dystans)
# najlepszej drogi. Wszystkie zapytania odnoszą się do tego samego grafu.
# Jakie rozwiązanie daje najlepszą klasę złożoności w każdym z poniższych przypadków?
#
# Q = O(1), E = O(V) - Dijkstra
# Q = O(1), E = O(V^2) - Dijkstra bez kolejki
# Q = O(V), E = O(V) - Q * Dijkstra
# Q = O(V), E = O(V^2) - Q * Dijkstra bez kolejki, Floyd-Warshall
#


from queue import PriorityQueue
from math import inf


def trafficJams(G, Q):
    result = []
    for q in Q:
        result.append(dijkstra(G, q[0], q[1]))
        # or dijkstraM or floydWarshall

    return result


def dijkstra(G, s, t):
    n = len(G)
    dpT = [inf for _ in range(n)]
    dpL = [inf for _ in range(n)]
    Q = PriorityQueue()

    dpT[s], dpL[s] = 0, 0
    Q.put((dpT[s], dpL[s], s))

    while not Q.empty():
        _, _, u = Q.get()

        for i in range(n):
            if G[u][i][0] > 0 and G[u][i][1] > 0 and dpT[i] > dpT[u] + G[u][i][0]:
                dpT[i] = dpT[u] + G[u][i][0]
                dpL[i] = dpL[u] + G[u][i][1]
                Q.put((dpT[i], dpL[i], i))

    return (dpT[t], dpL[t])


def dijkstraM(G, s, t):
    n = len(G)
    dpT = [inf for _ in range(n)]
    dpL = [inf for _ in range(n)]
    visited = [False for _ in range(n)]

    dpT[s], dpL[s] = 0, 0

    for i in range(n):

        u = minTimeDistance(dpT, dpL, visited)
        visited[u] = True

        for j in range(n):
            if G[u][j][0] > 0 and G[u][j][1] > 0 and dpT[j] > dpT[u] + G[u][j][0]:
                dpT[j] = dpT[u] + G[u][j][0]
                dpL[j] = dpL[u] + G[u][j][1]

    return (dpT[t], dpL[t])


def minTimeDistance(dpT, dpL, visited):
    minTime, minRoad, minIdx, n = inf, inf, 0, len(dpT)

    for i in range(n):
        if dpT[i] < minTime and visited[i] is False:
            minTime = dpT[i]
            minRoad = dpL[i]
            minIdx = i
        elif dpT[i] == minTime and dpL[i] < minRoad and visited[i] is False:
            minTime = dpT[i]
            minRoad = dpL[i]
            minIdx = i

    return minIdx


def floydWarshall(G, s, t):
    n = len(G)
    dpT = [[inf for _ in range(n)] for _ in range(n)]
    dpL = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j][1] != 0:
                dpT = G[i][j][0]
                dpL = G[i][j][1]

    for x in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    dpT[i][j] = min(dpT[i][j], dpT[i][x] + dpT[x][j])
                    dpL[i][j] = min(dpL[i][j], dpL[i][x] + dpL[x][j])

    return (dpT[s][t], dpL[s][t])
