# W Arktyce osady są oddalone od siebie na ogromne odległości. Otrzymujemy je jako pary współrzędnych (x, y).
# Niektóre z nich posiadają odbiorniki satelitarne - z takiej osady można bezpośrednio komunikować się z każdą
# inną osadą, która ma odbiornik satelitarny. Chcemy teraz w każdej osadzie umiejscowić radioodbiorniki o tym samym
# ograniczonym zasięgu D (liczba całkowita), aby można było się komunikować (pośrednio lub bezpośrednio) między każdą
# parą osad. Jakie jest minimalne D, które pozwoli osiągnąć ten cel?
# Uzasadnij poprawność rozwiązania.

# FloydWarshall gdzie poprawiawmy ściezki normalne na te które zawierają krótszą najdłuższą krawędź do danego wierzchołka

# Kruskal, najpierw liczymy odległości każdy z każdym wierzchołkiem, sortujemy rosnąco krawędzie po długości,
# tworzymy minimalne drzewo rozpinające, i rozwiązaniem jest najdłuższa krawędź z tego drzewa

# Łączymy wszystkie odbiorniki satelitarne w dowolne drzewo. Wystarczy je wstawić do jednego zbioru find-union,
# bo algorytm Kruskala sprawdza istnienie cyklu przez to, czy oba końce krawędzi są w tym samym zbiorze,
# alternatywnie możemy połączyć odbiorniki satelitarne krawędziami długości 0. Następnie uruchamiamy algorytm Kruskala.
# Znajdujemy najdłuższą krawędź w tym quasi-drzewie rozpinającym (pomijając krawędzie między odbiornikami satelitarnymi).
# Algorytm jest poprawny, bo Kruskal za każdym razem bierze najmniejszą możliwą krawędź, która nie tworzy cyklu


from math import ceil


def arcticWeb(L, S):
    n = len(L)
    edges = []

    for i in range(len(S)):
        for j in range(len(S)):
            edges.append(((i, j), 0))

    for a in range(n):
        for b in range(n):
            dist = ceil(calculateDistace(L[a], L[b]))
            edges.append(((a, b), dist))

    edges.sort(key=lambda x: x[1])

    m = len(edges)
    parents = [i for i in range(m)]
    rank = [0 for _ in range(m)]
    result = -1
    A = []

    for i in range(m):
        if find(edges[i][0][0], parents) != find(edges[i][0][1], parents):
            union(edges[i][0][0], edges[i][0][1], parents, rank)
            A.append(edges[i])
            if edges[i][1] > result:
                result = edges[i][1]

    return result


def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)

    if x == y: return 1
    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]


def calculateDistace(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** (1 / 2)
