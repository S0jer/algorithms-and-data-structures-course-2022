# Zadanie 2. (czy nieskierowany?) Proszę podać algorytm, który mając na wejściu graf G reprezentowany
# przez listy sąsiedztwa sprawdza, czy jest nieskierowany (czyli czy dla każdej krawędzie u → v istnieje także
# krawę dź przeciwna).


# Zamienić na reprezentację tablicową i sprawdzić czy M[i][j] == M[j][i] dla każdej potencjalnej krawędzi (n^2)


def notDirected(G):
    n = len(G)

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for exit in G[i]:
            dp[i][exit] = 1

    for a in range(n):
        for b in range(n):
            if dp[a][b] != dp[b][a]:
                return False

    return True


graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
G = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5, 6, 7], [3], [3], [3], [3, 8], [7]]

print(notDirected(graph))
print(notDirected(G))
