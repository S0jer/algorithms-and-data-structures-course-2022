# Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
# wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
# jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
# niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
# dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
# skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
# każdej z liczb.


from queue import PriorityQueue


def frog(T):
    n = len(T)
    queue = PriorityQueue()
    queue.put((-1 * T[0], 1))
    T[0] = -1

    while queue.empty():
        energy, cnt = queue.get()

        if energy >= n - 1:
            return cnt
        idx, maxEnergy = -1, -1
        for i in range(min(energy, n)):
            if T[i] > maxEnergy:
                maxEnergy = T[i]
                idx = i

        queue.put((energy + maxEnergy, cnt + 1))
        T[idx] = -1
