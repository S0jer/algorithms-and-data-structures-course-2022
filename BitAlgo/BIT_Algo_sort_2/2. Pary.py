# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te liczby na n par w taki sposób,
# że podział będzie miał najmniejszą maksymalną sumę liczb w parze. Przykładowo, dla liczb (1, 3, 5, 9) możemy mieć
# podziały ((1,3),(5,9)), ((1,5),(3,9)), oraz ((1,9),(3,5)). Sumy par dla tych podziałów to (4, 14),(6, 12) oraz (10, 8),
# w związku z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego, że ostatni podział ma najmniejszą maksymalną sumę.


# Sortujemy i parujemy: pierwszy-ostatni, drugi-przedostatni itd.
# Dowód: Załóżmy, że nasza strategia nie jest optymalna, tzn. da się tak połączyć elementy w pary, że maksymalna suma
# byłaby mniejsza. Oznaczmy przez (a[i], a[j]) parę o maksymalnej sumie wg oryginalnej strategii. Gdyby dało się połączyć
# elementy w pary, tak, że maksymalna suma byłaby mniejsza, oznaczałoby to, że a[i] musielibyśmy połączyć z a[k]: a[k] < a[j].
# Podobnie a[j] musielibyśmy połączyć z a[l]: < a[i]. W ten sposób zostanie bez pary więcej elementów większych od a[j]
# niż elementów mniejszych od a[i]. Będziemy więc musieli tak łączyć elementy w pary, że powstanie choć jedna para taka
# (a[x],a[y]), że a[x] > a[i] oraz a[y] > a[j], skąd a[x] + a[y] > a[i]+a[j], więc maksymalna suma jest większa
# niż w oryginalnej strategii. Sprzeczność.


def pairs(A):
    n = len(A)
    pairs = []

    quickSort(A, 0, n - 1)

    i, j = 0, n - 1
    while i < j:
        pairs.append((A[i], A[j]))
        i += 1
        j -= 1

    return pairs


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
