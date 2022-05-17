# Zadanie 7
# Dostając na wejściu string złożony z liter a-z, zwrócić najdłuższy jego fragment, który jest palindromem.
# Palindrom to ciąg znaków, który wygląda tak samo czytany zarówno od lewej, jak i od prawej strony.


# f(i, j) - czy S(i, j) jest palindromem

def palindrom(S):
    n = len(S)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
        if i + 1 < n and S[i] == S[i + 1]:
            dp[i][i + 1] = 1

    longestPalindrom = -1
    for j in range(n - 1):
        for i in range(1, n):

            if S[i - 1] == S[j + 1] and dp[i][j] == 1:
                if i == 2 and j == 2:
                    print(S[i - 1], S[j + 1], dp[i][j])
                dp[i - 1][j + 1] = 1
            if dp[i - 1][j + 1] == 1 and j - i + 3 > longestPalindrom:
                longestPalindrom = j - i + 3

    return longestPalindrom


S = 'alaamakotaakotmaale'
print(palindrom(S))
