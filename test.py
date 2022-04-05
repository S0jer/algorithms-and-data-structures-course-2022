# def activityNotifications(expenditure, d):
#     n = len(expenditure)
#     notifications = 0
#
#     for i in range(d - 1, n - 1):
#         e = expenditure[0:d]
#         print(e, expenditure)
#
#         # if d % 2 == 1:
#         #     median = select(e, i + 1 - d, (i + 1 - d + i + 1) // 2, i)
#         # else:
#         #     median = (select(e, i + 1 - d, (i + 1 - d + i + 1) // 2, i) + select(e, i + 1 - d,
#         #                                                                          (i + 1 - d + i + 1) // 2 - 1, i)) / 2
#         #
#         # if expenditure[i + 1] >= 2 * median:
#         #     notifications += 1
#
#     return notifications
#
#
# def partition(A, p, r):
#     x = A[r]
#     i = p - 1
#     for j in range(p, r):
#         if A[j] < x:
#             i += 1
#             A[j], A[i], = A[i], A[j]
#
#     A[r], A[i + 1] = A[i + 1], A[r]
#
#     return i + 1
#
#
# def quicksort(A, p, l):
#     while p < l:
#         q = partition(A, p, l)
#         quicksort(A, p, q - 1)
#         p = q + 1
#
#     return A
#
#
# def select(A, p, k, r):
#     if p == r: return A[p]
#     if p < r:
#         q = partition(A, p, r)
#         if q == k:
#             return A[q]
#         elif q < k:
#             return select(A, q + 1, k, r)
#         else:
#             return select(A, p, k, q - 1)


def activityNotifications(expenditure, d):
    n = len(expenditure)
    notifications = 0

    minHeap, maxHeap = [], []
    A = expenditure[0:d]
    quicksort(A, 0, len(A) - 1)
    if d % 2 == 1:
        median = A[d // 2]

        for i in range(len(A)):
            if A[i] >= median:
                minHeap.append(A[i])
            else:
                maxHeap.append(A[i])

        buildheap(maxHeap)
        buildheapMin(minHeap)

        for i in range(d, n):
            print(median, expenditure[i])
            if expenditure[i] >= 2 * median:
                notifications += 1

            if expenditure[i - d] >= median:
                deleteHeapMin(minHeap, expenditure[i - d])
            else:
                deleteHeap(maxHeap, expenditure[i - d])

            if expenditure[i] >= median:
                insertHeapMin(minHeap, expenditure[i])
            else:
                insertHeap(maxHeap, expenditure[i])

            if len(minHeap) - len(maxHeap) > 1:
                insertHeap(maxHeap, minHeap[0])
                deleteHeapMin(minHeap, minHeap[0])
            elif len(maxHeap) - len(minHeap) > 1:
                insertHeapMin(minHeap, maxHeap[0])
                deleteHeap(maxHeap, maxHeap[0])

            if len(minHeap) > len(maxHeap):
                median = minHeap[0]
            elif len(maxHeap) > len(minHeap):
                median = maxHeap[0]


    else:
        median = (A[d // 2] + A[d // 2 - 1]) / 2
        print(median)
        for i in range(len(A)):
            if A[i] >= median:
                minHeap.append(A[i])
            else:
                maxHeap.append(A[i])

        buildheap(maxHeap)
        buildheapMin(minHeap)

        for i in range(d, n):
            if expenditure[i] >= 2 * median:
                notifications += 1

            if expenditure[i] >= median:
                insertHeapMin(minHeap, expenditure[i])
            else:
                insertHeap(maxHeap, expenditure[i])

            if expenditure[i - d] >= median:
                deleteHeapMin(minHeap, expenditure[i - d])
            else:
                deleteHeap(maxHeap, expenditure[i - d])

            if len(minHeap) - len(maxHeap) > 1:
                insertHeap(maxHeap, minHeap[0])
                deleteHeapMin(minHeap, minHeap[0])
            elif len(maxHeap) - len(minHeap) > 1:
                insertHeapMin(minHeap, maxHeap[0])
                deleteHeap(maxHeap, maxHeap[0])

            median = (minHeap[0] + maxHeap[0]) / 2

    return notifications


def buildheapMin(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapifyMin(A, n, i)


def buildheap(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify(A, n, i)


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


def heapifyMin(A, n, i):
    l = left(i)
    r = right(i)
    min_ind = i

    if l < n and A[l] < A[min_ind]:
        min_ind = l
    if r < n and A[r] < A[min_ind]:
        min_ind = r
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapifyMin(A, n, min_ind)


def insertHeap(A, num):
    A.append(num)
    n = len(A) - 1
    p = parent(n)
    while p >= 0:
        if A[n] > A[p]:
            A[n], A[p] = A[p], A[n]
            n = p
            p = (n - 1) // 2
        else:
            break


def insertHeapMin(A, num):
    A.append(num)
    n = len(A) - 1
    p = parent(n)
    while p >= 0:
        if A[n] < A[p]:
            A[n], A[p] = A[p], A[n]
            n = p
            p = (n - 1) // 2
        else:
            break


def deleteHeapMin(A, num):
    A.remove(num)
    heapifyMin(A, len(A), 0)


def deleteHeap(A, num):
    A.remove(num)
    heapify(A, len(A), 0)


def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[j], A[i], = A[i], A[j]

    A[r], A[i + 1] = A[i + 1], A[r]

    return i + 1


def quicksort(A, p, l):
    while p < l:
        q = partition(A, p, l)
        quicksort(A, p, q - 1)
        p = q + 1

    return A


with open("file") as f:
    raw_data = f.read().strip().split("\n")
data = [eval(line) for line in raw_data]

d = 30000
r = activityNotifications(data, d)
print(r)
