# Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim równomiernie
# rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru.
# Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn. d = sqrt(x2 + y2).

# Równomiernie rozłożone tzn. bucket sort :)

def circle(points, k):
    n = len(points)
    bucketsCond = [0 for _ in range(n + 1)]
    for i in range(n):
        bucketsCond[i] = (((k ** 2) / n) + bucketsCond[i - 1] ** 2) ** (1 / 2)

    buckets = [[] for _ in range(n + 1)]

    for i in range(n):
        points[i] = (points[i][0], points[i][1], (points[i][0] ** 2 + points[i][1] ** 2) ** (1 / 2))
        idx = 0
        while True:
            if idx >= n + 1:
                return False
            if bucketsCond[idx - 1] <= points[i][2] <= bucketsCond[idx]:
                buckets[idx].append(points[i])
                break
            idx += 1
    print(points)

    for bucket in buckets:
        if len(bucket) > 1:
            selectionSort(bucket)

    result = []
    for b in buckets:
        for p in b:
            result.append(p)
    return result


def selectionSort(L):
    n = len(L)

    for i in range(n):
        minId = i
        for j in range(i + 1, n):
            if L[j][2] < L[minId][2]:
                minId = j

        L[i], L[minId] = L[minId], L[i]


points = [(4, 5), (2, -5), (7, -8), (-7, -7), (0, 1), (1, 2), (-1, 2), (3, 2), (-2, 3)]
k = 11

print(circle(points, k))
