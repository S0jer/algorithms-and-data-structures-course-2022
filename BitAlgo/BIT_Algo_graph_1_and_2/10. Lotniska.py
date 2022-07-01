# Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). Każda z nich oznacza, że możemy zbudować drogę między
# miastem A i B za podany koszt. Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta.
# Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
# Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
# Miasto ma dostęp do lotniska, jeśli:
# jest w nim lotnisko, lub
# można z niego dojechać do innego miasta, w którym jest lotnisko
# Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.


# Kruskal dla warunku że budujemy drogę tylko gdy dana droga jest tańsza niż wybudowanie lotniska, następnie w powstałych
# zbiorach budujemy lotnisko i stąd mamy minimalny koszt


def airport(E, K, N):
    n = len(E)
    result = 0
    airportsCnt = N
    E.sort(key=lambda x: x[2])

    parents = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    for i in range(n):
        if find(E[i][0], parents) != find(E[i][1], parents) and E[i][2] < K:
            union(E[i][0], E[i][1], parents, rank)
            result += E[i][2]
            airportsCnt -= 1

    result += airportsCnt * K

    return result


def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)

    if x == y: return 1
    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank(x) == rank[y]:
            rank[y] += 1


def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]
