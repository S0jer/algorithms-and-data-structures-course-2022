# Zaimplementuj algorytm Floyda-Warshalla tak, aby pozostawiał informację pozwalającą na  rekonstrukcję
# najkrótszej ścieżki między dwoma dowolnymi parami wierzchołków w czasie zależnym od długości tej ścieżki.


from math import inf


def floydWarshall(G):
    n = len(G)
    dp = [[inf for _ in range(n)] for _ in range(n)]
    parents = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                dp[i][j] = G[i][j]
                parents[i][j] = i

    for t in range(n):
        for a in range(n):
            for b in range(n):
                if a != b and dp[a][b] > dp[a][t] + dp[t][b]:
                    dp[a][b] = dp[a][t] + dp[t][b]
                    parents[a][b] = parents[t][b]

    return dp, parents


G = [[0, 4, 0, 0, 0, 3],
     [4, 0, 2, 0, 0, 4],
     [0, 2, 0, 4, 0, 2],
     [0, 0, 4, 0, 5, 0],
     [0, 0, 0, 5, 0, 7],
     [3, 4, 2, 0, 7, 0]]

print(floydWarshall(G))
