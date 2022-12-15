from egzP3btesty import runtests


def lufthansa(G):
    sumOfEdges, E, n = 0, [], len(G)
    edges = {(0, G[0][0][0], G[0][0][1])}

    for i in range(n):
        for e in G[i]:
            if i > e[0]:
                edges.add((e[0], i, e[1]))
            else:
                edges.add((i, e[0], e[1]))

    for e in edges:
        sumOfEdges += e[2]
        E.append(e)

    sumOfNotDeletedEdges = kruskal(E)

    return sumOfEdges - sumOfNotDeletedEdges


def kruskal(E):
    n, result, check = len(E), 0, 0
    parents = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    E.sort(key=lambda x: -1 * x[2])

    for i in range(n):
        if find(E[i][0], parents) != find(E[i][1], parents):
            union(E[i][0], E[i][1], parents, rank)
            result += E[i][2]
        elif check == 0:
            check = 1
            result += E[i][2]

    return result


def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)

    return parents[x]


def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)

    if x == y: return
    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


runtests(lufthansa, all_tests=True)
