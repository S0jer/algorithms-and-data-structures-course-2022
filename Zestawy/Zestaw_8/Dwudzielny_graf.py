# Czy graf jest dwuidzielny


from collections import deque


def BFS(graph, s):
    n = len(graph)
    Q = deque()

    v = [-1 for _ in range(n)]
    color = [0 for _ in range(n)]

    v[s] = 1
    color[s] = 1
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for i in range(n):
            if v[i] != 1 and graph[u][i] == 1:
                v[i] = 1
                Q.append(i)
            if color[u] == 1 and G[u][i] == 1:
                if color[i] == 1:
                    return False
                color[i] = -1
            elif color[u] == -1 and G[u][i] == 1:
                if color[i] == -1:
                    return False
                color[i] = 1

    return True


G = [[0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0]]

graph = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]]

print(BFS(graph, 0))
print(BFS(G, 0))
