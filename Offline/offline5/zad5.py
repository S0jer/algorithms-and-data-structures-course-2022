from zad5testy import runtests
from queue import PriorityQueue


# Paweł Jaśkowiec, 406165

# Algorytm polega na znajdowaniu największej wartości plamy oleju w zasięgu ruchu (0 ... [ilość paliwa])
# oraz dodawaniu danej wartości do koleji z ilością paliwa równą fuel + T[i], do momentu zgromadzenia ilości paliwa
# potrzebnej do dojechania do końca trasy T, przy czym dane miejsce zaznaczane jest na tablicy T
# wartością "-1" w celu odczytania trasy, zgodnie z kolejnością postojów

# Rozważałem również zapisywanie trasy na bieżąco co wymagało posortowania trasy gdy byliśmy w stanie dotrzeć
# do końca drogi bądź utrzymywania jej posortowanej podczas dodawania nowych miejsc tankowania ostatecznie
# decydując się na rozwiązanie z odczytaniem trasy z listy T

# Złożoność: n*log(n)


def plan(T):
    n = len(T)
    Q = PriorityQueue()
    Q.put((-1 * T[0], T[0]))
    T[0] = -1

    while not Q.empty():
        x, fuel = Q.get()
        maxF, idx = -1, -1
        if fuel >= n - 1:
            return getRoad(T, n)
        for i in range(0, min(fuel + 1, n)):
            if T[i] > maxF:
                maxF = T[i]
                idx = i
        Q.put((-1 * maxF, fuel + maxF))
        T[idx] = -1

    return []


def getRoad(T, n):
    result = []
    for j in range(n):
        if T[j] == -1:
            result.append(j)
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
