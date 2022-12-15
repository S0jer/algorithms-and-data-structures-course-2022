from egzP1atesty import runtests
from math import inf

# Dynamik, przechodzimy po słowie zamienionym na forme ".-.-....-" i następnie obliczamy funkcję
# f(i) - minimalna ilość liter użytych do wysłania słowa do i-tego znaku
# gdzie patrzymy 4 znaki do tyłu dla każdego znaku



def titanic(W, M, D):
    toDecode, dict = "", {}

    for i in range(len(W)):
        toDecode += M[ord(W[i]) - 65][1]
    n = len(toDecode)

    for j in D:
        dict[M[j][1]] = M[j][0]

    dp = [inf for _ in range(n)]

    for i in range(n):
        for j in range(i, max(-1, i - 4), -1):
            if len(toDecode[j:i + 1]) == 1 or dict.get(toDecode[j:i + 1]):
                if j - 1 >= 0:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
                else:
                    dp[i] = 1
    return dp[n - 1]


runtests(titanic, recursion=False)
