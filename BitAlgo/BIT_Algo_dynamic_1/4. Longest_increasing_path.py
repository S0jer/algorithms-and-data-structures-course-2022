# Zadanie 4
# Dostajemy tablicę (M x N) wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy (możemy
# przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy, że z pola o wartości 3, mogę przejść
# na pola o wartości większej bądź równej 4).
# Na początku wprowadzimy pewne ułatwienie:

# Mamy dany punkt początkow

# f(i, j) = max(f(i + 1, j), f(i, j + 1), f(i - 1, j), f(i, j + 1)) + 1
# f - długość najdłuższej ścieżki zaczynającej się w (i, j)
# dla odopwiednich warunków

# Wydaje mi się że zlicza za dużo w pewnych przypadkach ale nie udało mi się znaleźć błędu :(

from math import inf


def longestIncPathInBoard(A):
    n, m = len(A), len(A[0])
    dp = [[-inf for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if dp[i][j] < 0:

                if j > 0 and A[i][j] < A[i][j - 1] and dp[i][j - 1] < 0:
                    dp[i][j] = max(dp[i][j], f(i, j - 1, dp, A, 1))
                elif j > 0 and A[i][j] < A[i][j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)

                if j < m - 1 and A[i][j] < A[i][j + 1] and dp[i][j + 1] < 0:
                    dp[i][j] = max(dp[i][j], f(i, j + 1, dp, A, 1))
                elif j < m - 1 and A[i][j] < A[i][j + 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1])

                if i > 0 and A[i][j] < A[i - 1][j] and dp[i - 1][j] < 0:
                    dp[i][j] = max(dp[i][j], f(i - 1, j, dp, A, 1))
                elif i > 0 and A[i][j] < A[i - 1][j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)

                if i < n - 1 and A[i][j] < A[i + 1][j] and dp[i + 1][j] < 0:
                    dp[i][j] = max(dp[i][j], f(i + 1, j, dp, A, 1))
                elif i < n - 1 and A[i][j] < A[i + 1][j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + 1)

    result = -1
    for a in range(n):
        for b in range(m):
            if dp[a][b] > result:
                result = dp[a][b]

    for row in dp:
        print(row)

    return result


def f(i, j, dp, A, length):
    n, m = len(A), len(A[0])
    if i == 0 and j == 0:
        if dp[i][j + 1] > 0 and A[i][j] < A[i][j + 1]:
            length = max(length, dp[i][j + 1])
        elif A[i][j] < A[i][j + 1]:
            length = max(length, f(i, j + 1, dp, A, length))
        if dp[i + 1][j] > 0 and A[i][j] < A[i + 1][j]:
            length = max(length, dp[i + 1][j])
        elif A[i][j] < A[i + 1][j]:
            length = max(length, f(i + 1, j, dp, A, length))
    elif i == n - 1 and j == m - 1:
        if dp[i][j - 1] > 0 and A[i][j] < A[i][j - 1]:
            length = max(length, dp[i][j - 1])
        elif A[i][j] < A[i][j - 1]:
            length = max(length, f(i, j - 1, dp, A, length))
        if dp[i - 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i - 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i - 1, j, dp, A, length))
    elif i == 0 and j == m - 1:
        if dp[i][j - 1] > 0 and A[i][j] < A[i][j - 1]:
            length = max(length, dp[i][j - 1])
        elif A[i][j] < A[i][j - 1]:
            length = max(length, f(i, j - 1, dp, A, length))
        if dp[i + 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i + 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i + 1, j, dp, A, length))
    elif i == n - 1 and j == 0:
        if dp[i][j + 1] > 0 and A[i][j] < A[i][j + 1]:
            length = max(length, dp[i][j + 1])
        elif A[i][j] < A[i][j + 1]:
            length = max(length, f(i, j + 1, dp, A, length + 1))
        if dp[i - 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i - 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i - 1, j, dp, A, length + 1))

    elif i == 0 and m - 1 > j > 0:
        if dp[i][j - 1] > 0 and A[i][j] < A[i][j - 1]:
            length = max(length, dp[i][j - 1])
        elif A[i][j] < A[i][j - 1]:
            length = max(length, f(i, j - 1, dp, A, length))

        if dp[i][j + 1] > 0 and A[i][j] < A[i][j + 1]:
            length = max(length, dp[i][j + 1])
        elif A[i][j] < A[i][j + 1]:
            length = max(length, f(i, j + 1, dp, A, length))

        if dp[i + 1][j] > 0 and A[i][j] < A[i + 1][j]:
            length = max(length, dp[i + 1][j])
        elif A[i][j] < A[i + 1][j]:
            length = max(length, f(i + 1, j, dp, A, length))
    elif j == 0 and n - 1 > i > 0:
        if dp[i + 1][j] > 0 and A[i][j] < A[i + 1][j]:
            length = max(length, dp[i + 1][j])
        elif A[i][j] < A[i + 1][j]:
            length = max(length, f(i + 1, j, dp, A, length))

        if dp[i - 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i - 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i - 1, j, dp, A, length))

        if dp[i][j + 1] > 0 and A[i][j] < A[i][j + 1]:
            length = max(length, dp[i][j + 1])
        elif A[i][j] < A[i][j + 1]:
            length = max(length, f(i, j + 1, dp, A, length))
    elif i == n - 1 and m - 1 > j > 0:
        if dp[i - 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i - 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i - 1, j, dp, A, length))
        if dp[i][j + 1] > 0 and A[i][j] < A[i][j + 1]:
            length = max(length, dp[i][j + 1])
        elif A[i][j] < A[i][j + 1]:
            length = max(length, f(i, j + 1, dp, A, length))
        if dp[i][j - 1] > 0 and A[i][j] < A[i][j - 1]:
            length = max(length, dp[i][j - 1])
        elif A[i][j] < A[i][j - 1]:
            length = max(length, f(i, j - 1, dp, A, length))
    elif j == m - 1 and n - 1 > i > 0:
        if dp[i - 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i - 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i - 1, j, dp, A, length))
        if dp[i + 1][j] > 0 and A[i][j] < A[i + 1][j]:
            length = max(length, dp[i + 1][j])
        elif A[i][j] < A[i + 1][j]:
            length = max(length, f(i + 1, j, dp, A, length))
        if dp[i][j - 1] > 0 and A[i][j] < A[i][j - 1]:
            length = max(length, dp[i][j - 1])
        elif A[i][j] < A[i][j - 1]:
            length = max(length, f(i, j - 1, dp, A, length))

    elif n - 1 > i > 0 and m - 1 > j > 0:
        if dp[i][j - 1] > 0 and A[i][j] < A[i][j - 1]:
            length = max(length, dp[i][j - 1])
        elif A[i][j] < A[i][j - 1]:
            length = max(length, f(i, j - 1, dp, A, length))

        if dp[i][j + 1] > 0 and A[i][j] < A[i][j + 1]:
            length = max(length, dp[i][j + 1])
        elif A[i][j] < A[i][j + 1]:
            length = max(length, f(i, j + 1, dp, A, length))

        if dp[i + 1][j] > 0 and A[i][j] < A[i + 1][j]:
            length = max(length, dp[i + 1][j])
        elif A[i][j] < A[i + 1][j]:
            length = max(length, f(i + 1, j, dp, A, length))

        if dp[i - 1][j] > 0 and A[i][j] < A[i - 1][j]:
            length = max(length, dp[i - 1][j])
        elif A[i][j] < A[i - 1][j]:
            length = max(length, f(i - 1, j, dp, A, length))

    if n > i > -1 and m > j > -1:
        dp[i][j] = max(dp[i][j], length)

    return length + 1


T = [[1, 4, 5, 76, 3],
     [2, 7, 8, 31, 3],
     [3, 6, 9, 21, 3],
     [4, 5, 19, 20, 3],
     [1, 4, 5, 5, 3],
     [1, 4, 5, 76, 3]]

print(longestIncPathInBoard(T))
