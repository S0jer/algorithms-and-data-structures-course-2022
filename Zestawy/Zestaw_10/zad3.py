# Zadanie 3. (wymiana walut) Dana jest tabela kursów walut. Dla każdych dwóch walut x oraz y wpis
# K[x][y] oznacza ile trzeba zapłacić waluty x żeby otrzymać jednostkę waluty y. Proszę zaproponować algorytm,
# który sprawdza czy istnieje taka waluta z, że za jednostkę z można uzyskać więcej niż jednostkę z
# przez serię wymian walut.


from math import inf, log


# If you find decreasing cycle in a graph where you change values to log(value) then it means there exists
# a way to get more of a certain currency by few exchanges

def moneyExchange(G):
    n = len(G)

    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                G[i][j] = log(G[i][j])

    for i in range(n):
        if bellmanFord(G, i):
            return True

    return False


def bellmanFord(G, s):
    n = len(G)
    dp = [inf for _ in range(n)]
    parents = [-1 for _ in range(n)]
    dp[s] = 0

    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                if G[i][j] > 0 and dp[j] > dp[i] + G[i][j]:
                    dp[j] = dp[i] + G[i][j]
                    parents[j] = i

    for i in range(n):
        for j in range(n):
            if dp[i] > dp[j] + G[i][j] and G[i][j] > 0:
                return True

    return False


G = [[0, 2, 1, 1, 3],
     [3, 0, 1, 4, 9],
     [1, 1, 0, 3, 1],
     [1, 4, 3, 0, 5],
     [3, 9, 1, 5, 0]]

print(moneyExchange(G))
