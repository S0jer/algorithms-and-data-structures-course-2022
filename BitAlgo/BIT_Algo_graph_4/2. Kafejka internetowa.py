# W kafejce internetowej jest K komputerów i A aplikacji na płytach CD. Na każdym komputerze może być zainstalowana
# maksymalnie jedna aplikacja. Każda aplikacja ma listę komputerów na których może działać, a na pozostałych nie może
# z powodu wymagań sprzętowych. Jesteś właścicielem kafejki i wiesz, ilu klientów (możliwie zero) będzie chciało jutro
# skorzystać z danej aplikacji. Zakładamy, że każdy klient zajmuje komputer na cały dzień.
# Jaką aplikację powinieneś zainstalować na każdym z komputerów, aby wszyscy klienci mogli skorzystać z tej aplikacji,
# którą chcą? Jeżeli takie przyporządkowanie nie istnieje, algorytm powinien to stwierdzić.

# Tworzymy siec na zasadzie po lewej stronie aplikacje po prawej stronie komuptery, aplikacje łączymy z komputerami
# na ktorych można uruchomić dane aplikacje krawędziami o wadze 1, następnie do aplikacji dołączamy źródło krawędziami
# o wartościach równych danym ile danej aplikacji będzie klienci chcieli użyć dnia następnego
# a komputery łączymy z ujściem krawędziami o wadze 1 i uruchamiamy algorytm maksymalnego przepływu:
# Ford-Fulkerson/Edmonds-Karp


import copy, collections


def webCafe(K, A, schedudle):
    n, m = len(A), len(K)
    graph = [[0 for _ in range(n + m + 2)] for _ in range(n + m + 2)]
    for i in range(n):
        for j in range(len(A[i])):
            graph[i][A[i][j] + n] = 1

    for j in range(n, n + m):
        graph[j][n + m + 1] = 1

    for x in range(len(schedudle)):
        graph[n + m][x] = schedudle[x]

    maxFlow = edmonds_karp(graph, n + m, n + m + 1)

    if maxFlow == sum(schedudle):
        return True
    return False


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


K = [0, 1, 2, 3, 4, 5]
A = [(0, 1, 2),
     (0, 4),
     (3, 4, 5),
     (0, 5)]

schedudle = [3, 1, 2, 0]
schedudle1 = [3, 1, 2, 3]

print(webCafe(K, A, schedudle))
print(webCafe(K, A, schedudle1))
