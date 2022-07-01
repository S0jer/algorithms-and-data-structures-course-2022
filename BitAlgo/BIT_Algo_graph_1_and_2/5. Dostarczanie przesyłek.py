# Bajtocja jest krainą zawierającą N miast, N - 1 dwukierunkowych dróg  i układ dróg tworzy graf spójny. Mając
# listę K miast do których musimy dostarczyć przesyłki i mogąc wystartować i zakończyć trasę w dowolnym mieście,
# podaj minimalny dystans który musmy przebyć.

# Dany graf to drzewo !


# Z miasta z listy K szukamy BFS'em miasta najbardziej oddalonego od niegoz listy K, następnie dla znalezionego miasta
# szukamy najdalej leżaącego miasta z listy K i przechodząc po trasie między tymi dwoma miastami zliczamy długości
# ścieżek na boki do reszty miast z K i otrzymujemy minimalny dystans jaki musimy przebyć.


from queue import Queue


def package(G, K):
    n, m = len(G), len(K)
    visited = [-1 for _ in range(n)]

    parents, distance, _ = BFS(G, K[0], visited[::])
    kMaxStart = findFurthestVertex(distance)
    parents, distance, _ = BFS(G, kMaxStart, visited[::])
    kMaxEnd = findFurthestVertex(distance)

    road = getRoad(parents, kMaxEnd)
    result = len(road) - 1

    for r in road:
        if r in K:
            K.remove(r)
        visited[r] = 1

    for r in road:
        _, roadLen = DFS(G, r, visited[::], 0, K, False)
        result += 2 * roadLen

        if len(K) <= 0:
            break

    return result


def DFS(G, u, visited, roadLength, K, found):
    n = len(G)
    visited[u] = 1
    if u in K:
        found = True

    for i in range(n):
        if G[u][i] > 0 and visited[i] != 1:
            found, roadLength = DFS(G, i, visited, roadLength, K, found)
            if found and u not in K:
                roadLength += 1

    return found, roadLength


def BFS(G, s, visited):
    n = len(G)
    parents = [-1 for _ in range(n)]
    distance = [-1 for _ in range(n)]
    distance[s] = 0
    visited[s] = 1

    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for i in range(n):
            if visited[i] == -1 and G[u][i] > 0:
                visited[i] = 1
                distance[i] = distance[u] + 1
                parents[i] = u
                Q.put(i)

    return parents, distance, visited


def getRoad(parents, k):
    road = [k]
    while parents[k] != -1:
        road.append(parents[k])
        k = parents[k]

    return road


def findFurthestVertex(distance):
    kMax, kMaxDistance = -1, -1
    for k in K:
        if distance[k] > kMaxDistance:
            kMaxDistance = distance[k]
            kMax = k

    return kMax


G = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

G2 = [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

K = [4, 5, 9]
K2 = [6, 5, 9, 7]
print(package(G2, K2))
