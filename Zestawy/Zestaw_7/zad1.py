# Zadanie 1. (pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
from math import inf


def pointsCoverage(X):
    cnt, start, n = 0, -inf, len(X)

    for i in range(n):
        if start <= X[i] <= start + 1:
            continue
        else:
            cnt += 1
            start = X[i]

    return cnt


X = [0.25, 0.5, 1.6]
print(pointsCoverage(X))
