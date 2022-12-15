from egzP9btesty import runtests
from queue import Queue
import sys





def dyrektor(G, R):
    n = len(G)

    graph = [[] for _ in range(n)]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    dictR = [{} for _ in range(n)]

    for i in range(n):
        for e in R[i]:
            if dictR[i].get(e) is None:
                dictR[i][e] = 1
            else:
                dictR[i][e] += 1

    edgeCnt = 0
    for i in range(n):
        for e in G[i]:
            if dictR[i].get(e) is None or dictR[i][e] == 0:
                # graph[i].append((e, edgeCnt))
                graph[i][e] += 1
                edgeCnt += 1
            if dictR[i].get(e) is not None and dictR[i].get(e) > 0:
                dictR[i][e] -= 1

    visited = {}
    result = DFS(graph, 0, visited, [])

    if result is not None:
        return result[::-1]
    return []


def DFS(G, s, visited, road):
    n = len(G)
    for e in range(n):
        if G[s][e] > 0:
            G[s][e] -= 1
            # visited[e[1]] = True
            DFS(G, e, visited, road)

    road.append(s)

    return road



runtests(dyrektor, all_tests=True)
