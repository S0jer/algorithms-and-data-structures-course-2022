# Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce przebyć trasę z punktu A
# do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
# się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
# łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
# wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
# punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.


from math import inf
from queue import PriorityQueue


def tankHowMuchYouWant(G, price, s, k, D):
    n = len(G)
    finalCost = inf
    visited = [False for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, D, s, [s]))

    while not Q.empty():
        cost, fuel, u, road = Q.get()
        visited[u] = True

        for i in range(n):
            if D >= G[u][i] > 0 and visited[i] is False:
                if price[i] >= price[u]:
                    Q.put((cost + (D - fuel) * price[u], D - G[u][i], i, road + [i]))
                elif price[u] > price[i]:
                    if fuel - G[u][i] >= 0:
                        Q.put((cost, fuel - G[u][i], i, road + [i]))
                    else:
                        Q.put((cost + (G[u][i] - fuel) * price[u], 0, i, road + [i]))

        if u == k and cost < finalCost:
            finalCost = cost
            finalRoad = road

    return finalRoad, finalCost


def tankFull(G, price, s, k, D):
    n = len(G)
    finalCost = inf
    visited = [False for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, D, s, [s]))

    while not Q.empty():
        cost, fuel, u, road = Q.get()
        visited[u] = True

        for i in range(n):
            if D >= G[u][i] > 0 and visited[i] is False:
                if price[i] >= price[u] or fuel - G[u][i] < 0:
                    Q.put((cost + (D - fuel) * price[u], D - G[u][i], i, road + [i]))
                elif price[u] > price[i] and fuel - G[u][i] >= 0:
                    Q.put((cost, fuel - G[u][i], i, road + [i]))

        if u == k and cost < finalCost:
            finalCost = cost
            finalRoad = road

    return finalRoad, finalCost


G = [[0, 4, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 3, 7, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3],
     [0, 0, 0, 0, 0, 0, 0, 6, 0, 4, 0, 8],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0]]

price = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021]

print(tankHowMuchYouWant(G, price, 0, 8, 7))
print(tankFull(G, price, 0, 8, 7))
