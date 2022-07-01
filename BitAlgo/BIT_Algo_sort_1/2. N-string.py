# Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje
# tę tablicę w czasie O(n). Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.


# Bucket sort i radix ale na zasadzie takiej że w bucketach sortujemy po ostaniej literce i łączymy z bucketem
# zawierającym krótsze słowa i tak do długości 1


def nString(strings):
    n = len(strings)
    m = 0

    for i in range(n):
        m = max(m, len(strings[i]))

    buckets = [[] for _ in range(m + 1)]

    for i in range(n):
        buckets[len(strings[i])].append(strings[i])

    result = []
    idx = n - 1
    while idx > 0:
        if len(buckets[idx]) > 0:
            result = buckets[idx] + result
            radixSort(result, idx - 1)
        idx -= 1

    return result


def radixSort(L, idx):
    minus = 65
    toSortList = [[] for _ in range(59)]
    result = []
    for i in range(len(L)):
        toSortList[ord(L[i][idx]) - minus].append(L[i])

    for s in toSortList:
        result += s

    return result


strings = ["pawel", "ala", "dominika", "kot", "tomek", "ok", "xd", "liga", "kamper"]

print(nString(strings))
