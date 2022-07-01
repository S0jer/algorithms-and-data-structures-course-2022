# Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based heap).
# Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x.


# Nieoptymalnie: sprawdzać elementy po kolei metodą pop() - O(k*log(n)).
# Optymalnie:
# Zauważmy, że z definicji kopca minimum każdy korzeń poddrzewa jest mniejszy od wszystkich swoich dzieci. Dotyczy
# to zarówno korzenia całego kopca, jak i wszystkich poddrzew. Wynika z tego, że jeżeli korzeń jest >= x, to całe
# poddrzewo musi być >= x (skoro nic nie może być tam mniejszego, to może być tylko większe lub równe).
# Zauważmy także, że nie interesuje nas wartość wierzchołków przed k-tym. Co więcej, nie interesuje nas nawet wartość
# k-tego wierzchołka - interesuje nas tylko jego relacja z x, czy jest od niego mniejszy, czy większy lub równy.
# Można przejść po drzewie kopca (przydatne są tutaj funkcje pomocnicze get_left_child(i), get_right_child(i) oraz
# get_parent(i)) przeszukując dzieci wszystkich wierzchołków o wartości mniejszej od x, aż:
# znajdziemy przynajmniej k wierzchołków o wartości < x; jeżeli tak się stanie, to k-ty wierzchołek musiał być mniejszy
# od x, a więc zwracamy fałsz
# wyczerpiemy wierzchołki o wartości < x, zanim znaleźliśmy ich k; jeżeli tak się stanie, to dalsze wierzchołki
# muszą być >= x, a zatem k-ty też, więc zwracamy prawdę

# Złożoność: sprawdzamy tylko dzieci wierzchołków o wartości < x, a tych jest co najwyżej k (jeżeli byłoby więcej,
# to przerywamy zgodnie z opisem powyżej); każde może mieć co najwyżej 2 dzieci, więc odwiedzamy co najwyżej
# 3k wierzchołków, a więc mamy O(k).


from queue import Queue


def isBigger(A, x, k):
    Q = Queue()
    Q.put(0)

    while k > 0:
        idx = Q.get()
        Q.put(left(idx))
        Q.put(right(idx))

        if A[idx] >= x:
            return True
        else:
            k -= 1

    return False


def buildHeap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    maxIdx = i

    if l < n and A[l] < A[maxIdx]:
        maxIdx = l
    if r < n and A[r] < A[maxIdx]:
        maxIdx = r
    if maxIdx != i:
        A[i], A[maxIdx] = A[maxIdx], A[i]
        heapify(A, n, maxIdx)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


A = [9, 5, 4, 8, 6, 3, 1, 2, 7]
buildHeap(A)

print(isBigger(A, 2, 1))
