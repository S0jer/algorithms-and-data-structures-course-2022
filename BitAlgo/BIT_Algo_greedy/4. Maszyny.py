# W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem.
# Prowincję można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę,
# a wartość 0, że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i,
# to miasta o indeksach j takich, że abs(i-j) < k są przez nią chronione. Należy zaproponować algorytm, który
# stwierdzi ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe.


def machines(A, k):
    n = len(A)
    machines = []
    for i in range(n):
        if A[i] == 1:
            machines.append((i, max(0, i - k + 1), min(n, i + k - 1)))

    qSort(machines, 0, len(machines) - 1, 1)

    result = []
    i, j, m = 0, 0, len(machines)
    if machines[i][0] > 0:
        return -1
    while i < m:
        result.append(machines[i])
        j += 1
        if machines[i][2] > machines[j][1]:
            return -1
        while j < m and machines[i][2] >= machines[j][1]:
            j += 1
        i = j

    if result[-1][2] < n - 1:
        return -1

    for i in range(len(result)):
        result[i] = result[i][0]

    return result


def qSort(A, p, r, idx):
    while p < r:
        q = partition(A, p, r, idx)
        qSort(A, p, q - 1, idx)
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
