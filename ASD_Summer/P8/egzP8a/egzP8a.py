from egzP8atesty import runtests
import bisect


# maksymalny zysk jaki mozna uzyskac od 0 do i-tego dnia,


def reklamy(T, S, o):
    n = len(T)
    dp = [0 for _ in range(n)]

    for i in range(n):
        T[i] = (T[i][0], T[i][1], S[i])
    T.sort(key=lambda x: x[0])

    result = 0
    dp[n - 1] = T[n - 1][2]

    for i in range(n - 2, -1, -1):
        dp[i] = max(dp[i + 1], T[i][2])

    S = [T[i][0] for i in range(n)]

    for i in range(n):
        end = T[i][1]
        idx = bisect.bisect_right(S, end, lo=i + 1)

        second = 0
        if idx < n and S[idx] != end:
            second = dp[idx]
        result = max(result, T[i][2] + second)

    return result


runtests(reklamy, all_tests=True)
