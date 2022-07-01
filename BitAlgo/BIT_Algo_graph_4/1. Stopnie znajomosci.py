# Definiujemy relację znajomości między osobami jako symetryczną.
# Znajomość:
# pierwszego stopnia to bezpośrednia znajomość osoby
# drugiego stopnia to bycie “znajomym znajomego” osoby, ale nie bezpośrednim znajomym osoby
# trzeciego, czwartego, piątego stopnia, itd.
# nieskończonego stopnia zachodzi wtedy gdy nie ma ciągu znajomości, który łączyłby dwie osoby
# Mając na wejściu listę osób i znajomości pierwszego stopnia między nimi,
# chcemy znaleźć największy stopień znajomości wśród każdej z możliwych par.
# Znajdź optymalne rozwiązanie zarówno dla grafów rzadkich (|E| = O(|V|)), jak i gęstych (|E| = O(|V|^2)


# Tworzymy graf z listy znajomości a następnie:

# Problem sprowadza się do:
# sprawdzenia spójności grafu - jeżeli graf jest niespójny, to największy stopień znajomości jest nieskończony
# jeżeli graf jest spójny - znalezienia długości najdłuższej ścieżki (lub średnicy) grafu.
# Ponieważ krawędzie są wagi 1, to:
#
#  - dla grafu rzadkiego (E = O(V)) najlepszym rozwiązaniem jest wywołanie BFSa z każdego wierzchołka: V*O(V+E) =V*O(V+V) =  O(V^2)
#
#  - dla grafu gęstego (E = O(V^2)) możemy użyć BFSa z każdego wierzchołka V*O(V+E) =V*O(V+V^2) =  V*O(V^2) = O(V^3)
# lub algorytmu Floyda-Warshalla O(V^3). Floyd-Warshall ma krótszą implementację i daje mniej okazji na pomylenie się
#
# Zarówno BFS, jak i Floyd-Warshall pozwalają na sprawdzenie spójności grafu - w BFSie sprawdzamy, czy po pojedynczym
# wywołaniu wszystkie wierzchołki są visited, a we Floydzie-Warshallu - czy w macierzy pojawia się odległość nieskończoność.


from math import inf
from queue import Queue


def familiarityLevelBfs(people, familiarityList):
    n = len(people)
    # Uproszczenie tzn osoby jaki indeksy, pomijam przypisywanie osoby do indeksu
    G = [[0 for _ in range(n)] for _ in range(n)]
    result = -1

    for f in familiarityList:
        G[f[0]][f[1]] = 1

    for i in range(n):
        visited = [-1 for _ in range(n)]
        dp = [-1 for _ in range(n)]
        Q = Queue()

        dp[i] = 0
        Q.put(i)

        while not Q.empty():
            u = Q.get()
            visited[u] = 1

            for j in range(n):
                if G[u][j] > 0 and visited[j] != 1:
                    dp[j] = dp[u] + 1
                    Q.put(j)

        if sum(visited) < n:
            return False

        tmp = max(dp)
        if tmp > result:
            result = tmp

    return result


def familiarityLevelFloyd(people, familiarityList):
    n = len(people)
    G = [[-1 for _ in range(n)] for _ in range(n)]
    dp = [[inf for _ in range(n)] for _ in range(n)]

    for f in familiarityList:
        G[f[0]][f[1]] = 1
        G[f[0]][f[0]] = 0
        G[f[1]][f[1]] = 0

    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                dp[i][j] = G[i][j]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    dp[i][j] = min(dp[i][j], dp[i][t] + dp[t][j])

    result = -1
    for a in range(n):
        for b in range(n):
            if dp[a][b] > result:
                result = dp[a][b]

    if result == inf:
        return False

    return result


people = [0, 1, 2, 3, 4, 5, 6, 7, 8]

familiarityList = [(0, 1), (0, 7), (1, 0), (1, 2), (1, 6), (2, 1), (3, 7), (4, 6), (5, 6), (6, 1), (6, 4), (6, 5),
                   (7, 0), (7, 3),
                   (7, 8), (8, 7)]

print(familiarityLevelBfs(people, familiarityList))
print(familiarityLevelFloyd(people, familiarityList))
