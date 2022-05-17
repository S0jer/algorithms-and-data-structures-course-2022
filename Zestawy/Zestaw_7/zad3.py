# Zadanie 3. (ładowanie przyczepy) Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków
# o wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków
# wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i
# uzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
# (ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się
# np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając
# jednego ładunku, to lepsze jest to pierwsze rozwiązanie).


# Przyczepę ładujemy największym możliwym ładunkiem, ponieważ ze względu na to że wagi są potęgami

def trailerLoading(Weights, K):
    result, n = [], len(Weights)
    T = sorted(Weights, reverse=True)

    for w in T:
        if w <= K:
            result.append(w)
            K -= w

    return result


K = 27
Weights = [16, 8, 4, 4, 2, 1, 1]

print(trailerLoading(Weights, K))
