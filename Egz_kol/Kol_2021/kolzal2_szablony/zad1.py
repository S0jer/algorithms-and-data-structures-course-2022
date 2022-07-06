from zad1testy import runtests
from math import inf

# Bierzemy jakikolwiek prostokat i szukamy takiego z ktorym ma on najmniejsze wspolne pole
# Nastepnie dla tego znalezionego szukamy znowu danego z ktorym bedzie on mial najmniejsze pole
# Porownujemy bez ktorego pole wspolne jest wieksz, wyrzucamy drugi



def rect(D):
    n = len(D)
    minIdxP = -1

    minP = inf
    for i in range(n):
        x = (min(D[0][2], D[i][2]) - max(D[0][0], D[i][0]))
        y = (min(D[0][3], D[i][3]) - max(D[0][1], D[i][1]))
        p = x * y
        if p <= minP:
            minP = p
            minIdxP = i

    minP = inf
    for i in range(n):
        x = (min(D[minIdxP][2], D[i][2]) - max(D[minIdxP][0], D[i][0]))
        y = (min(D[minIdxP][3], D[i][3]) - max(D[minIdxP][1], D[i][1]))
        p = x * y
        if p <= minP:
            minP = p
            minIdxP2 = i

    xMin, yMin, xMax, yMax, xMin2, yMin2, xMax2, yMax2 = -inf, -inf, inf, inf, -inf, -inf, inf, inf
    p1, p2 = 0, 0

    for i in range(n):
        if i != minIdxP:
            xMin = max(D[i][0], xMin)
            yMin = max(D[i][1], yMin)
            xMax = min(D[i][2], xMax)
            yMax = min(D[i][3], yMax)
        if i != minIdxP2:
            xMin2 = max(D[i][0], xMin2)
            yMin2 = max(D[i][1], yMin2)
            xMax2 = min(D[i][2], xMax2)
            yMax2 = min(D[i][3], yMax2)

    if yMax - yMin > 0 and xMax - xMin > 0:
        p1 = (yMax - yMin) * (xMax - xMin)
    if yMax2 - yMin2 > 0 and xMax2 - xMin2 > 0:
        p2 = (yMax2 - yMin2) * (xMax2 - xMin2)

    if p1 > p2:
        return minIdxP
    else:
        return minIdxP2


runtests(rect)
