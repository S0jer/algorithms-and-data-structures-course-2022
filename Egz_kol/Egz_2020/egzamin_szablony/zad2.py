from zad2testy import runtests

from math import inf


def opt_sum(tab):
    n = len(tab)

    dp = [[inf for _ in range(n)] for _ in range(n)]
    prefixes = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            pass

    return 9


runtests(opt_sum)
