from queue import PriorityQueue



def jakdojade(G, P, d, a, b):
    n = len(G)
    Q = PriorityQueue()

    Q.put((0, a, d, [a]))

    while not Q.empty():
        rLen, u, fuel, road = Q.get()

        for i in range(n):
            if -1 < G[u][i] <= d and u in P:
                Q.put((rLen + G[u][i], i, d - G[u][i], road + [i]))
            elif -1 < G[u][i] <= fuel:
                Q.put((rLen + G[u][i], i, fuel - G[u][i], road + [i]))

        if u == b:
            return road

    return None


def getRoad(parents, t):
    road = [t]
    while t != -1:
        road.append(parents[t])
        t = parents[t]

    return road[::-1]


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]

P = [0, 1, 3]

print(jakdojade(G, P, 5, 0, 2))
# [0, 3, 2]
print(jakdojade(G, P, 6, 0, 2))
# [0, 1, 2]
print(jakdojade(G, P, 3, 0, 2))
# None
