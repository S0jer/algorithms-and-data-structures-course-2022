from kolutesty import runtests
from collections import deque


# Na bazie tablicy depends tworzysz listową reprezentację grafu oraz tablicę Prevs,
# która dla każdego programu przechowa ilość jego poprzedników (len(depends[i])). Inicjalizujesz dwa stosy,
# z czego jeden na programy z dyskietki A, a drugi na programy z dyskietki B. Do stosów dodajesz programy mające
# 0 poprzedników. Przypuśćmy, że zaczynasz od dyskietki A - zdejmujesz programy z odpowiedniego stosu, przy czym
# zdejmując program wirtualnie "kasujesz" krawędzie z niego wychodzące (tak naprawdę zmniejszasz o 1 pola tablicy
# Prevs dla tych programów, które są następnikami właśnie zdejmowanego). Jeżeli podczas tej kasacji jakikolwiek nowy
# program osiągnął wartość 0 w swoim polu w tablicy Prevs, dodajesz go na stos wg odpowiedniej dyskietki (stał się on
# dostępny do instalacji). Zdejmujesz programy ze stosu do momentu, aż ten stanie się pusty - w tym momencie zmieniasz
# stos, wkładasz dyskietkę B i zaczynasz analogicznie zdejmować programy z drugiego stosu. Tego typu swapy dyskietek
# (stosów) stosujesz do momentu, aż obydwa stosy staną się puste. Ilość zamian stosów to minimalna liczba zamian
# dyskietek podczas serii instalacji (poczynając od dykietki A). Następnie powtarzasz ten sam algorytm, ale zaczynając
# od dyskietki B. Wynikiem jest minimum z ilości zamian podczas dwóch procesów zaczynających się od dyskietek A i B.
# Złożoność wychodzi O(n), bo ilość operacji na stosach (i wcześniejszego preprocessingu) jest liniowa względem ilości
# zależności między programami, czyli krawędziami grafu (w zasadzie to O(n + m), gdzie m to ilość programów.


def countSwaps(depCount, G, diskId, dnm):
    swapsCnt, n = 0, len(depCount)
    heaps = [deque() for _ in range(2)]
    for i in range(n):
        if depCount[i] == 0:
            heaps[diskId[i]].append(i)

    d = dnm
    while heaps[d]:
        while heaps[d]:
            x = heaps[d].pop()
            for e in G[x]:
                depCount[e] -= 1
                if depCount[e] == 0:
                    heaps[diskId[e]].append(e)
        d = (d + 1) % 2
        swapsCnt += 1

    for x in depCount:
        if x != 0:
            swapsCnt = 0

    return swapsCnt - 1


def swaps(disk, depends):
    n = len(depends)
    G = [[] for _ in range(n)]
    diskId = [0 for _ in range(n)]
    depCount = [0 for _ in range(n)]

    for i in range(n):
        depCount[i] = len(depends[i])
        if disk[i] == 'A':
            diskId[i] = 0
        else:
            diskId[i] = 1
        for k in depends[i]:
            G[k].append(i)

    r1 = countSwaps(depCount[:], G, diskId, 0)
    r2 = countSwaps(depCount[:], G, diskId, 1)

    if r1 == -1:
        return r2
    if r2 == -1:
        return r1

    return min(r1, r2)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(swaps, all_tests=True)
