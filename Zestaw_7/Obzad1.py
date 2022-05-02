# Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi;
# A jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
# (1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
# (2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za litr paliwa).
# Na każdej stacji możemy tankować dowolną ilość paliwa.
# (3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna.


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


def minTankB():




    pass



L = 10
S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 44]
P = [1.2, 2.1, 3.4, 5.2, 1.4, 4.20, 1.337, 2.115, 9.97, 6.9, 2.5, 2.021]
t = 47

# L = 10
# S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# P = [2, 1, 2, 3, 3, 1, 1, 3, 2, 2, 1, 2, 2, 3, 2, 3, 3, 1, 1, 2]
# t = 21

print(minTankA(t, S, L))
