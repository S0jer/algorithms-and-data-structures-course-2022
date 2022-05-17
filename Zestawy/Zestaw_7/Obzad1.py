# Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi;
# A jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# (1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna. # minTankA
# (2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za litr paliwa).
# Na każdej stacji możemy tankować dowolną ilość paliwa. # minTankB
# (3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna. # minTankB2Dynamic
from math import inf


# Tankujemy w najdalszej stacji do jakiej możemy dojechać

def minTankA(meta, Stations, tank):
    tankCounter, fuel, idx = 0, tank, -1
    position = 0

    while position + fuel < meta:
        if idx >= 0 and Stations[idx + 1] - Stations[idx] > tank:
            return False
        elif position + tank < Stations[0]:
            return False

        while idx + 1 < len(Stations) and fuel - (Stations[idx + 1] - position) >= 0:
            idx += 1
        tankCounter += 1
        position = Stations[idx]
        fuel = tank

    return tankCounter


# Tankujemy w najtańszej stacji do jakiej możemy dojechać, tzn jeśli na niej jesteśmy to
# tankujemy do pełna jeśli jest ona przed nami to tankujemy tyle aby do niej dojechać.

def minTankB(meta, Stations, Price, tank):
    n = len(Stations)
    oilPrice, fuel, positionIdx = 0, tank, 0
    fuel -= Stations[0]

    while positionIdx < n - 1 and Stations[positionIdx] < meta:
        if Stations[positionIdx] + fuel >= meta:
            return oilPrice

        if Stations[positionIdx + 1] - Stations[positionIdx] > tank:
            return False

        idx = positionIdx + 1
        minIdx = idx
        minPrice = Stations[idx]
        while idx < n and tank >= (Stations[idx] - Stations[positionIdx]):
            if Price[idx] < minPrice:
                minPrice = Price[idx]
                minIdx = idx
            idx += 1

        if Price[positionIdx] > Price[minIdx]:
            if fuel >= (Stations[minIdx] - Stations[positionIdx]):
                fuel -= (Stations[minIdx] - Stations[positionIdx])
                oilPrice += (tank - fuel) * Price[minIdx]
                fuel = tank
                positionIdx = minIdx
            else:
                toTank = (Stations[minIdx] - Stations[positionIdx]) - fuel
                oilPrice += toTank * Price[positionIdx]
                fuel = 0
                positionIdx = minIdx
        else:
            oilPrice += (tank - fuel) * Price[positionIdx]
            fuel = tank
            fuel -= (Stations[minIdx] - Stations[positionIdx])
            positionIdx = minIdx

    if Stations[positionIdx] + fuel >= meta:
        return oilPrice
    elif Stations[positionIdx] + tank >= meta:
        oilPrice += (meta - Stations[positionIdx] - fuel) * Price[positionIdx]
        return oilPrice
    else:
        return False


def minTankB2Dynamic(meta, Stations, Price, tank):
    oilPrice, n, result = inf, len(Stations), inf
    dp = [inf for _ in range(n + 1)]
    print(Stations)
    Stations, Price = [0] + Stations, [0] + Price
    print(Stations[n])
    dp[0] = 0

    for i in range(1, n + 1):
        j = i - 1
        while j >= 0 and Stations[i] - Stations[j] <= tank:
            dp[i] = min(dp[i], dp[j] + (Stations[i] - Stations[j]) * Price[i])
            j -= 1

    j = n
    while meta - Stations[j] <= tank:
        result = min(result, dp[j])
        j -= 1

    return result


L = 10
S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 42]
P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021]
t = 45

# L = 10
# S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# P = [2, 1, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 3, 3, 1, 1, 2]
# t = 21

print(minTankB2Dynamic(t, S, P, L))
