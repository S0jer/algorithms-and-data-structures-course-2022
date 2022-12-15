# Zadanie 1. (SAT-2CNF) Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest
# koniunkcją klauzuli, gdzie każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej
# negacja. Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest: (x ∨ y) ∧ (x ∨ z) ∧ (z ∨ y).
# Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie spełniające formułę.


# Tworzymyu graf gdzie całość formuły to ostatni wierzchołek

def SAT2CNF(formula):
    Orrs = formula.split("∧")
    for i in formula:
        print(i, ord(i))
    values = {i for i in formula if 65 <= ord(i) < 123}
    values = list(values)
    n = len(values) + len(Orrs) + 1
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(values)):
        for j in range(len(Orrs)):
            for k in range(len(Orrs[j])):
                graph[len(values) + j][n - 1] = 1
                if values[i] == Orrs[j][k] and Orrs[j][k - 1] == "-":
                    graph[i][len(values) + j] = -1
                elif values[i] == Orrs[j][k]:
                    graph[i][len(values) + j] = 1

    for row in graph:
        print(row)


# Res thought about using some kind of BFS or maybe max flow algorithm that check "or's" for -1 and 1 values from
# x,y,z etc. and count if every "or" returns positive result in last vertex, the formula is correct if value
# in last vertex is equal to "Orrs" length

# Maybe gonna write that solution later :)


formula = "(x ∨ y) ∧ (-x ∨ z) ∧ (-z ∨ -y)"

print(SAT2CNF(formula))
