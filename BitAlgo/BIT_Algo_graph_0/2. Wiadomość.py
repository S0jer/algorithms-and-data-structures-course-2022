# Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n - 1.
# Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych przekazuje
# tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.
# Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.

from queue import Queue


def message(connections, n):
    G = [[] for _ in range(n)]
    for i in range(len(connections)):
        G[connections[i][0]].append(connections[i][1])
        G[connections[i][1]].append(connections[i][0])

    visited = [False for _ in range(n)]
    messCnt = [0 for _ in range(n + 1)]

    Q = Queue()

    Q.put((1, 0))

    while not Q.empty():
        day, u = Q.get()
        if visited[u] is False:
            messCnt[day] += 1
        visited[u] = True

        for i in G[u]:
            if visited[i] is False:
                Q.put((day + 1, i))

    result = (-1, -1)
    for i in range(n + 1):
        if messCnt[i] > result[1]:
            result = (i, messCnt[i])

    return result


pairs = [
    (0, 1),
    (0, 3),
    (3, 2),
    (2, 4),
    (2, 5),
    (2, 6),
    (4, 5),
    (5, 6),
    (5, 7),
    (5, 8)
]

print(message(pairs, 9))
