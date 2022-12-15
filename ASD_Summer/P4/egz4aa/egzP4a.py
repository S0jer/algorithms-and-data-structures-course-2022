from egzP4atesty import runtests


def mosty(T):
    # print(T)
    n = len(T)
    T.sort()
    result = lis(T)

    return result


def lis(A):
    n, maxi = len(A), 0
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i][0] > A[j][0] and A[i][1] > A[j][1] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i

    return F[maxi]


# def index(A, l, r, key):
#     while r - l > 1:
#         m = l + (r - l) // 2
#
#         if A[m][0] >= key[0] and A[m][1] >= key[1]:
#             r = m
#         else:
#             l = m
#     return r
#
#
# def lis(A):
#     n = len(A)
#     tailTable = [(0, 0) for _ in range(n + 1)]
#     length = 0
#
#     tailTable[length] = A[length]
#     length += 1
#
#     for i in range(1, n):
#         if A[i][0] < tailTable[0][0] and A[i][1] < tailTable[0][1]:
#             tailTable[0] = A[i]
#
#         elif A[i][0] > tailTable[length - 1][0] and A[i][1] > tailTable[length - 1][1]:
#             tailTable[length] = A[i]
#             length += 1
#         else:
#             tailTable[index(A, -1, length - 1, A[i])] = A[i]
#
#     return length


runtests(mosty, all_tests=True)
