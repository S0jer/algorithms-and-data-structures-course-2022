from egzP7btesty import runtests


def ogrod(S, V):
    n, m = len(S), len(V)
    result = 0

    for i in range(n):
        S[i] -= 1

    for i in range(n):
        taken = [-1 for _ in range(n)]
        tmpResult = 0
        for j in range(i, n):
            if taken[S[j]] == -1:
                tmpResult += V[S[j]]
                taken[S[j]] = 1
            elif taken[S[j]] == 1:
                result = max(result, tmpResult)
                tmpResult -= V[S[j]]
                taken[S[j]] = 2
            elif taken[S[j]] == 2:
                pass
        result = max(result, tmpResult)

    return result


runtests(ogrod, all_tests=True)
