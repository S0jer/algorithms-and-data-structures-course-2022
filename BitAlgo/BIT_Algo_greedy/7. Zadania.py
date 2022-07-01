# Dana jest lista zleceń. Każde zlecenie wymaga pewnego kapitału początkowego Ci, który należy mieć, żeby zacząć
# zlecenie oraz zysk Pi, który doda się do naszego całkowitego kapitału, gdy wykonamy zlecenie. Mając kapitał
# początkowy W i liczbę k wybierz co najwyżej k zleceń tak, że skończysz z maksymalnym możliwym kapitałem.
# Przykład: k = 2, W = 0, P=[1,2,3], C=[0,1,1]. Rozwiązanie: na początku mamy kapitał 0, więc możemy wybrać tylko
# zlecenie pierwsze. Po jego ukończeniu mamy kapitał równy 1, więc możemy wybrać albo zlecenie 2 albo 3. Zlecenie
# 3 ma większy profit więc wybieramy zlecenie 3, ponieważ możemy wybrać już tylko 1 zlecenie (k = 2).
# Kończymy z kapitałem 4.


import heapq
from queue import PriorityQueue


def findMaximizedCapital(k, W, Profits, Capital):
    current = []
    future = sorted(zip(Capital, Profits))[::-1]
    for _ in range(k):
        while future and future[-1][0] <= W:
            heapq.heappush(current, -future.pop()[1])
        if current:
            W -= heapq.heappop(current)
    return W


def tasks(P, C, k, W):
    n = len(P)
    T = []

    for i in range(n):
        T.append((P[i], C[i]))

    quickSort(T, 0, n - 1, 0)
    quickSort(T, 0, n - 1, 1)
    Q = PriorityQueue()

    for _ in range(k):
        idx = 0
        while idx < len(T) and T[idx][1] <= W:
            Q.put((-1 * T.pop(idx)[0]))
        if not Q.empty():
            W -= Q.get()

    return W


def quickSort(A, p, r, idx):
    while p < r:
        q = partition(A, p, r, idx)
        quickSort(A, p, q - 1, idx)
        p = q + 1


def partition(A, p, r, idx):
    x = A[r][idx]
    i = p - 1

    for j in range(p, r):
        if A[j][idx] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


k = 2
W = 0
P = [1, 2, 3]
C = [0, 1, 1]

print(findMaximizedCapital(k, W, P, C))
print(tasks(P, C, k, W))
