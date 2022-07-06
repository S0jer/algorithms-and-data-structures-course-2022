from zad2testy import runtests


def order(L, K):
    n = len(L)
    M = 10 ** K
    moduloL, divideL = [0 for _ in range(n)], [0 for _ in range(n)]
    used = [False for _ in range(n)]

    for i in range(n):
        moduloL[i] = (L[i] % M, i)
        divideL[i] = (L[i] // M, i)

    moduloL = countingSort(moduloL, M)
    divideL = countingSort(divideL, M)

    print(moduloL)
    print(divideL)

    # idxM, idxL, result = 0, 0, []
    #
    # while idxL < n and idxM < n:
    #     if used[moduloL[idxL][1]] is False:
    #         result.append(L[moduloL[idxL][1]])
    #
    #     if moduloL[idxL][0] != divideL[idxM][0] and moduloL[idxL][1] != divideL[idxM][1]:
    #         return None
    #
    #     if used[divideL[idxM][1]] is False:
    #         result.append(L[divideL[idxM][1]])
    #     idxL += 1
    #
    #     if moduloL[idxL][0] != divideL[idxM][0] and moduloL[idxL][1] != divideL[idxM][1]:
    #         return None
    #
    #     idxM += 1

    return result

def countingSort(A, M):
    n = len(A)
    buck = [[] for _ in range(M)]
    result = []

    for i in range(n):
        buck[A[i][0]].append(A[i])

    for b in buck:
        result += b

    return result


runtests(order)
