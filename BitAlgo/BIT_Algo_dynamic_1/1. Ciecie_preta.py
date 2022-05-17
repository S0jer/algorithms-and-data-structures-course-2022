# Zadanie 1: Cięcie pręta
# Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. Kawałki mają długość w metrach wyrażoną
# zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n metrów.
# Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.

# Zadanie 2
# Zmodyfikuj rozwiązanie problemu cięcia stalowych prętów tak, aby konstruowało i zwracało także rozwiązanie, tj. listę
# długości prętów o największej cenie.
# Podpowiedź: bottom-up będzie łatwiej


# Zadanie 1 + 2
# f(i) - maksymalna cena pręta o długości i


def cut(n, prices):
    dp = [0 for _ in range(n + 1)]
    parents = [[i] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i] = prices[i]
        for j in range(i + 1):
            if prices[j] + dp[i - j] > dp[i]:
                dp[i] = prices[j] + dp[i - j]
                parents[i] = [i for i in parents[i - j]]
                parents[i].append(j)

    return dp[n], parents[n]


prices = [0, 1, 2, 4, 5, 1, 3, 4]
n = 7
print(cut(n, prices))
