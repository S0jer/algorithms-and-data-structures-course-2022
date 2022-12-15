from egzP5atesty import runtests


def inwestor(T):
    n = len(T)
    heap = [-1, 0]

    result = 0

    LS = [-1 for _ in range(n)]
    RS = [n for _ in range(n)]

    for i in range(1, n):
        while heap[len(heap) - 1] != -1 and T[heap[len(heap) - 1]] > T[i]:
            RS[heap[len(heap) - 1]] = i
            heap.pop()

        if T[i] == T[i - 1]:
            LS[i] = LS[i - 1]
        else:
            LS[i] = heap[len(heap) - 1]

        heap.append(i)

    for j in range(0, n):
        result = max(result, T[j] * (RS[j] - LS[j] - 1))

    return result


runtests(inwestor, all_tests=True)
