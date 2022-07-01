# Mamy pewien układ klocków domino. Otzrymujemy go w postaci list par [a, b]. Jeżeli przewrócimy klocek a, to klocek b
# też się przewróci. Checemy znaleźć minimalną liczbę klocków, które trzeba przewrócić ręcznie, aby wszystkie domina były
# przewrócone.


# Tworzymy graf skierowany z listy L a następnie sortujemy topologicznie
# Po kolejności otrzymanej z sortowania topologicznego uruchamami DFS aż odwiedzimy wszystkie wierzchołki
# wynikiem jest liczba wywołan DFS'a,
# Można odwrócić krawędzie i znaleźć silnie spójne składowe, wychodzi na to samo

def domino(L):
    n = -1
    for l in L:
        n = max(n, max(l))
    n += 1
    indexes = [-1 for _ in range(n)]
    tmp = 0
    for l in L:
        if indexes[l[0]] == -1:
            indexes[l[0]] = tmp
            tmp += 1
        if indexes[l[1]] == -1:
            indexes[l[1]] = tmp
            tmp += 1

    graph = [[0 for _ in range(tmp)] for _ in range(tmp)]

    for l in L:
        graph[indexes[l[0]]][indexes[l[1]]] = 1

    visited = [-1 for _ in range(tmp)]
    topSort = []
    for i in range(n):
        if visited[indexes[i]] == -1 and indexes[i] != -1:
            visited, d = DFS(graph, indexes[i], visited, [])
            topSort.append(d[::-1])

    cnt = 0
    visited = [-1 for _ in range(tmp)]

    for el in topSort:
        for e in el:
            if visited[e] == -1:
                visited, d = DFS(graph, e, visited, [])
                cnt += 1

    return cnt


def DFS(G, u, visited, d):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if G[u][i] > 0 and visited[i] != 1:
            visited, d = DFS(G, i, visited, d)

    d.append(u)

    return visited, d


L = [(1, 2), (2, 3), (2, 1), (4, 7), (5, 7), (6, 7), (4, 6), (5, 4), (6, 5)]

print(domino(L))
