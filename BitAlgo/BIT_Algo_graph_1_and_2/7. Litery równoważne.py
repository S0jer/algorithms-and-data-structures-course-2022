# Dostajemy na wejściu trzy stringi: A, B i C. A i B są tej samej długości. Zachodzą następujące właściwości:
# Litery na tym samym indeksie w stringach A i B są równoważne
#
# Jeżeli litera a jest równoważna z literą b, to litera b jest równoważna z literą a
# Jeżeli litera a jest równoważna z b, a litera b z literą c, to litera a jest równoważna z literą c
# Każda litera jest równoważna sama ze sobą
#
# W stringu C możemy zamienić dowolną literę z literą do niej równoważną. Jaki jest najmniejszy leksykograficznie string,
# który możemy w tej sposób skonstruować?

# Ze słowa A oraz B za pomocą union, find tworzymy zbiory o swoich reprezentantach a następnie
# każda litere ze słowa C zastępujemy jeśli to możliwe (tzn. należy do jednego ze zbiorów stworzonych przez union)
# reprezentatnem zbioru do którego należy dana litera. union/find uwzględniające jako reprezentanta leksykograficznie
# najmnijesza literę


def letters(A, B, C):
    m = 124
    lettersIdx = [-1 for _ in range(m)]
    rank = [0 for _ in range(m)]
    parents = [-1 for _ in range(m)]

    for i in range(len(A)):
        if lettersIdx[ord(A[i])] == -1:
            lettersIdx[ord(A[i])] = ord(A[i])
            parents[ord(A[i])] = ord(A[i])

        if lettersIdx[ord(B[i])] == -1:
            lettersIdx[ord(B[i])] = ord(B[i])
            parents[ord(B[i])] = ord(B[i])
        x = max(ord(A[i]), ord(B[i]))
        y = min(ord(A[i]), ord(B[i]))
        union(x, y, parents, rank)

    newString = ""

    for c in C:
        newC = find(ord(c), parents)
        if newC == -1:
            newString += c
        else:
            newString += chr(find(ord(c), parents))

    return newString


def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)

    if x == y: return 1
    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]


A = "abefz"
B = "bceea"
C = "abcdefgz"

print(letters(A, B, C))
