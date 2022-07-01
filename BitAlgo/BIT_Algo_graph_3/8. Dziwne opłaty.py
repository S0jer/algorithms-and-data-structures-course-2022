# Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana.
# Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata. Od tej kwoty jest jednak
# odejmowany całkowity koszt poniesiony od początku podróży (jeśli jest ujemny, po prostu nic się nie płaci).
#
# Np. na trasie 1-2-3-5 opłaty wyniosą kolejno: 60+20+0, a na trasie 1-4-5 będzie to 120+30
#
# Mając dane:
#  - graf połączeń w dowolnej reprezentacji (nieskierowany, ważony)
#  - numery stacji początkowej i docelowej
#
# Oblicz minimalny koszt przejechania tej trasy.


# Ten sposób liczneie jest równoważny z tym że cena przejazdu daną trasą jest równa najdroższej krawędzie na trasie,
# więc dijkstra z modyfikacją liczącą koszt dotarcia jako najdroższa krawędź na trasie z s -> t


from queue import PriorityQueue
from math import inf


def strangePayments(G, s, t):
    n = len(G)
    Q = PriorityQueue()
    dp = [inf for _ in range(n)]

    dp[s] = 0
    Q.put((dp[s], s))

    while not Q.empty():
        v, u = Q.get()

        for i in range(n):
            cost = max(G[u][i], v)
            if G[u][i] > 0 and cost < dp[i]:
                dp[i] = cost
                Q.put((cost, i))

    return dp[t]


G = [[0, 50, 60, 0, 0, 0, 0],
     [50, 0, 0, 120, 90, 0, 0],
     [60, 0, 0, 0, 0, 50, 0],
     [0, 120, 0, 0, 0, 80, 70],
     [0, 90, 0, 0, 0, 0, 40],
     [0, 0, 50, 80, 0, 0, 140],
     [0, 0, 0, 70, 40, 140, 0]]

print(strangePayments(G, 0, 6))
