# Pewien znany profesor zaprosił Cię na spotkanie w Magicznym Mieście. W mieście tym niektóre drogi mogą być uczęszczane
# tylko przez ludzi poniżej 30 roku życia (w tym Ciebie), inne tylko przez ludzi w wieku od 30 lat (w tym profesora).
# Są też drogi, które mogą być uczęszczane przez każdego. Każda z dróg ma określoną długość, wyrażoną dodatnią liczbą
# naturalną, może być jedno- lub dwukierunkowa. Drogi te łączą możliwe lokalizacje spotkania. Wśród nich wyróżniamy
# mieszkanie Twoje i mieszkanie profesora.
# Profesor prosi Cię, byś wybrał takie miejsce na spotkanie, aby łączna droga, którą musicie pokonać Ty i profesor była
# jak najmniejsza. Jeżeli jest więcej niż jedno takie miejsce, podaj je wszystkie. Jeżeli takie miejsce nie istnieje,
# algorytm również powinien to stwierdzić.

# Budujemy dwa grafy bądź na jednym rozróżniami typy dróg
# Dijkstra od profesora i od ucznia (2xDijkstra) / BFS na ważonych (możemy użyć bo "dodatnia liczba naturalna")
# Suma wyników Dijkstry od profesora i od ucznia
# Miejsce gdzie suma jest minimalna / lista takich miejsc
# Jesli same inf'y to nie ma takiego miejsca


from queue import PriorityQueue
from math import inf


def professorMeeting(G1, G2, p, s):
    n = len(G1)
    dProf = dijkstry(G1, p)
    dStud = dijkstry(G2, s)

    result = []
    minDist = inf

    for i in range(n):
        dist = dProf[i] + dStud[i]
        if minDist > dist:
            minDist = dist
            result = [i]
        elif minDist == dist:
            result.append(i)

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
