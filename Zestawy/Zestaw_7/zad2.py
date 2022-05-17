
# Zadanie 2. (wybór zadań z terminami) Mamy dany zbiór zadań T = {t1, . . . , tn}. Każde zadanie ti
# dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
# terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie
# wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane
# zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
# do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.


# Sortujemy tablicę T po zyskach a nastepnie idąc po największych zyskach dodajemy na pierwsze wolne
# miejsce z wolnym, odpowiednim terminem realizacji

def tasks(T, time):
    n = len(T)
    dp = [0 for _ in range(time)]
    T = sorted(T, key=lambda x: x[0], reverse=True)
    print(T)

    for i in range(n):
        profit, deadline = T[i][0], T[i][1]
        if deadline >= time:
            deadline = time - 1
        while deadline >= 0 and dp[deadline] != 0:
            deadline -= 1
        if dp[deadline] < profit:
            dp[deadline] = profit

    return sum(dp)


T = [(5, 8), (4, 7), (4, 5), (3, 4), (1, 4), (2, 2)]
time = 4

print(tasks(T, time))
