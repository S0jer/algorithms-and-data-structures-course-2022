# Zadanie 5. (suma odległości) Dana jest posortowana tablica A zawierająca n liczb i celem jest wyznaczenie
# liczby x takiej, że wartość ∑n−1 i=0  ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić
# jego poprawność oraz ocenić złożoność obliczeniową.

# Szukamy mediany :)


def median(T):
    n = len(T)
    if n % 2 == 0:
        return (T[n//2] + T[n//2 + 1])/2
    else:
        return T[n//2]


T = [1, 3, 5, 6, 8, 9, 10]

print(median(T))


