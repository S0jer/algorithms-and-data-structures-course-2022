# Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza,
# że kantor kupi n waluty2 za kurs*n waluty1.
# Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
# Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie
# i kończymy z większą ilością pieniędzy niż zaczynaliśmy?


# Tworzymy z listy graf oraz zamieniamy wagi krawędzi na logarytmy,
# następnie szukamy za pomoca algorytmu Bellmana-Forda ujemnego cyklu
# i odczytujemy jego trasę


from math import inf, log


def exchange(W):
    n = -1
    for w in W:
        n = max(n, w[0], w[1])
    n += 1
    graph = [[-inf for _ in range(n)] for _ in range(n)]
    for w in W:
        graph[w[0]][w[1]] = log(w[2])

    for s in range(n):
        dp = [inf for _ in range(n)]
        parents = [-1 for _ in range(n)]
        dp[s] = 0

        for k in range(n - 1):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] != -inf and dp[j] > dp[i] + graph[i][j]:
                        dp[j] = dp[i] + graph[i][j]
                        parents[j] = i

        for i in range(n):
            for j in range(n):
                if dp[i] > dp[j] + graph[i][j] and graph[i][j] != -inf:
                    return True

    return False


W = [(0, 1, 4.5),
     (0, 2, 0.5),
     (2, 0, 2.5),
     (0, 3, 2.5),
     (1, 3, 1.5),
     (1, 4, 0.5),
     (2, 4, 3.5),
     (3, 4, 1),
     (4, 1, 2)]

print(exchange(W))
