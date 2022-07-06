from zad2testy import runtests


def tower(A):
    n = len(A)
    dp = [0 for _ in range(n)]

    for i in range(n):
        idx = i
        while idx >= 0:
            if A[idx][0] <= A[i][0] and A[idx][1] >= A[i][1]:
                dp[i] = max(dp[i], dp[idx] + 1)
            idx -= 1



    return max(dp)

runtests(tower)
