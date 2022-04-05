from zad3testy import runtests


# Paweł Jaśkowiec, 406165

# Działanie algorytmu polega na podzieleniu tablicy T na przedziały o długości range = (maxT - minT) / n
# a następnie posortowanie danych przedziałów sortowaniem insertion sort,
# mozemy rozwiązać dane zadanie w ten sposób ponieważ liczby z każdego przedziału
# z tablicy P zostały wylosowane zgodnie z rozkładem jednostajnym, gdzie prawdopodobieństwa
# można pominąć a co za tym idzie stosujemy w tym zadaniu po prostu Bucket sort'a

# Złożoność: O(n) dla jednostajnego rozkładu
#            O(n^2) gdy nie ma jednostajnego rozkładu


def SortTab(T, P):
    n = len(T)
    maxT = max(T) + 1
    minT = min(T) - 1
    rangee = (maxT - minT) / n

    sections = [[] for _ in range(n)]

    for i in range(n):
        idx = (T[i] - minT) / rangee
        sections[int(idx)].append(T[i])

    T = []
    for j in range(n):
        insertionSort(sections[j])
        T += sections[j]

    return T


def insertionSort(A):
    n, idx = len(A), 0

    for i in range(1, n):
        u = A[i]
        j = i - 1
        while j >= 0 and A[j] > u:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = u

    return A


runtests(SortTab)
