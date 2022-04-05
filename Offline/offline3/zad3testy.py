# zad3testy.py
from testy import *
from zad3test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(T, P):
    if len(P) > 100:
        P = P[:100]
    out = ', '.join([f'({a}, {b}, {c:.3f})' for a, b, c in P])
    print("Wejciowe przedzialy:\t", limit(out))

    if len(T) > 100:
        T = T[:100]
    out = ', '.join([f'{x:.3f}' for x in T])
    print("Wejciowa tablica:\t", limit(out))


def printhint( hint ):
    if len(hint) > 100:
        hint = hint[:100]
    out = ', '.join([f'{x:.3f}' for x in hint])
    print("Prawidlowy wynik:\t", limit(out))


def printsol( sol ):
    if len(sol) > 100:
        sol = sol[:100]
    out = ', '.join([f'{x:.3f}' for x in sol])
    print("Wynik algorytmu:\t", limit(out))


def check( L, P, hint, sol ):
    good = True

    if len(hint) != len(sol):
        print("Błąd! Nieprawidlowa liczba elementow w wyniku")
        good = False
    else:
        for i, elem in enumerate(zip(hint, sol)):
            if elem[0] != elem[1]:
                print(f'Błąd! Nieprawidlowa liczba na pozycji {i}')
                good = False
                break

    return good

 
def runtests( f ):
    TESTS = []
    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    internal_runtests( copyarg, printarg, printhint, printsol, check, TESTS, f, ALLOWED_TIME )

