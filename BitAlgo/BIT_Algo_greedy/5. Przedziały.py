# Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru, taki że:
# - jego rozmiar wynosi dokładnie k
# - przedziały są rozłączne
# - różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna.
# Jeśli rozwiązanie nie istnieje, to algorytm powinien to stwierdzić. Algorytm powinien być w miarę możliwości szybki,
# ale przede wszystkim poprawny.


# Dla każdego przedziału znajdujemy inny przedział, taki że nie zachodzą na siebie i różnica między początkiem
# pierwszego i końcem drugiego jest minimalna. Następnie próbujemy spacerować po tak znalezionych sąsiadach i sprawdzamy,
# czy udało nam się przejść k przedziałów.


def intervals(interv, k):
    n = len(interv)
    pairs = [[i] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if interv[i][0] > interv[j][1] or interv[i][1] < interv[j][0]:
                if len(pairs[i]) > 1 and abs(interv[pairs[i][1]][1] - interv[i][0]) > abs(interv[j][1] - interv[i][0]):
                    pairs[i][1] = j
                else:
                    pairs[i].append(j)

    for i in range(n):
        used = [-1 for _ in range(n)]
        curr = interv[i][0]
        result = []
        cnt = k
        while cnt > 0:
            if used[curr] == 1:
                break
            else:
                result.append(curr)
                used[curr] = 1
                curr = interv[curr][1]
                cnt -= 1
        if len(result) == k:
            return result

    return -1
