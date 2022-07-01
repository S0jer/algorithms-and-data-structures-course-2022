# W problemie coin change mamy daną kwotę X i chcemy ją rozmienić na monety o wartości 1, 5, 10, 25 i 100.
# Podaj algorytm, który obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz ile sztuk każdej monety będzie
# trzeba użyć. Można założyć, że każdej monety mamy nieskończenie wiele sztuk.
# Czy algorytm zachłanny działa dla zestawu monet 1, 2, 7, 10? Jeśli tak, uzasadnij dlaczego. Jeśli nie, podaj kontrprzykład.


# Bierzemy monetę o największej wartości, odejmujemy jej wartość od X, szukamy znowu (byle tylko wartość monety
# nie przekraczała aktualnie poszukiwanej wartości).
#
# Dla kwoty X = 5...9 lepiej wybrać piątkę i kilka jedynek niż więcej jedynek
# Dla kwoty X = 10...25 lepiej wybrać tyle dziesiątek ile się da niż zastępować dziesiątki zestawem dwóch piątek,
# jednej piątki i pięciu jedynek
# Dla kwoty X > 25 lepiej wybrać tyle 25-ek ile się da niż zastępować je mniejszymi nominałami
#
# Kontrprzykład dla drugiego zestawu monet: 15 = 7 + 7 + 1 = 10 + 2 + 2 + 1. Dla tego zestawu problem można rozwiązać dynamicznie.


def coinExchangeDynamic(coins, x):
    dp = [i for i in range(x + 1)]
    dp[0] = 0

    for i in range(1, x + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[x]


def coinExchangeGreedy(coins, x):
    n = len(coins) - 1
    cnt = 0
    quickSort(coins, 0, n)

    while x > 0:
        while x - coins[n] >= 0:
            cnt += 1
            x -= coins[n]
        n -= 1

    return cnt


def quickSort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        p = q + 1


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


A = [1, 5, 100, 25, 10]
B = [1, 2, 7, 10]

print(coinExchangeGreedy(A, 30))
print(coinExchangeDynamic(A, 30))
print(coinExchangeDynamic(B, 30))
