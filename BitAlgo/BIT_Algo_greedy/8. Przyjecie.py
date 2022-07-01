# Alicja chce zorganizować przyjęcie i zastanawia się, kogo zaprosić spośród n znajomych. Stworzyła już listę par osób
# które się znają. Chce wybrać możliwie jak najwięcej osób, tak aby spełnione były dwa warunki: na przyjęciu każda osoba
# powinna znać co najmniej 5 osób oraz co najmniej 5 osób nie znać.
# Zaproponuj algorytm który przyjmuje na wejściu listę n osób oraz listę par osób które się znają,
# a na wyjściu daje możliwie najdłuższą listę gości.

# Zachłannie usuwamy osoby niespełniające warunków


def party(guests, connections, k):
    n = len(guests)

    countConnections = [[0, []] for _ in range(n)]

    for c in connections:
        countConnections[c[0]][0] += 1
        countConnections[c[0]][1].append(c[1])
        countConnections[c[1]][0] += 1
        countConnections[c[1]][1].append(c[0])

    deleted = True
    while deleted:
        deleted = False
        for i in range(n):
            if 0 < countConnections[i][0] < k:
                deleted = True
                for toDel in countConnections[i][1]:
                    countConnections[toDel][0] -= 1
                    countConnections[toDel][1].remove(i)
    result = []
    for j in range(n):
        if countConnections[j][0] >= k:
            result.append(j)

    return result
