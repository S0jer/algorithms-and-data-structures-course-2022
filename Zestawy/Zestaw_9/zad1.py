# Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie,
# przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym.
# Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.

# Not my implementation
def HamiltonianPath(adj):
    N = len(adj)
    dp = [[False for _ in range(1 << N)]
          for _ in range(N)]

    # Set all dp[i][(1 << i)] to
    # true
    for i in range(N):
        dp[i][1 << i] = True

    # Iterate over each subset
    # of nodes
    for i in range(1 << N):
        for j in range(N):

            # If the jth nodes is included
            # in the current subset
            if ((i & (1 << j)) != 0):

                # Find K, neighbour of j
                # also present in the
                # current subset
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                            adj[k][j] == 1 and
                            j != k and
                            dp[k][i ^ (1 << j)]):
                        # Update dp[j][i]
                        # to true
                        dp[j][i] = True
                        break

    # Traverse the vertices
    for i in range(N):

        # Hamiltonian Path exists
        if (dp[i][(1 << N) - 1]):
            return True

    # Otherwise, return false
    return False


# My implementation using topologic sort
def hamPath(G):
    n = len(G)

    for i in range(n):
        sorTp, visited = DFSTP(G, [False for _ in range(n)], i, [])

        if len(sorTp) == n and canTraverse(G, sorTp):
            return True

    return False


def DFSTP(G, visited, u, sorTp):
    n = len(G)
    visited[u] = True

    for i in range(n):
        if G[u][i] > 0 and visited[i] is False:
            DFSTP(G, visited, i, sorTp)

    sorTp.append(u)

    return sorTp[::-1], visited


def canTraverse(G, path):
    idx, n = 0, len(G)

    while idx < n - 1:
        if G[path[idx]][path[idx + 1]] == 0:
            return False
        idx += 1

    return True


adj = [[0, 1, 1, 1, 0],
       [1, 0, 1, 0, 1],
       [1, 1, 0, 1, 1],
       [1, 0, 1, 0, 0]]

G = [[0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 1, 0, 0]]

print(hamPath(adj))
print(HamiltonianPath(adj))
print()
print(hamPath(G))
print(HamiltonianPath(G))
