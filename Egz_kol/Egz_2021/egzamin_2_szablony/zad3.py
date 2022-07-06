from zad3testy import runtests


def lamps(n, T):
    colors = [0 for _ in range(n)]
    maxBlue, blue = -1, 0

    for t in T:
        for i in range(t[0], t[1] + 1):
            colors[i] = (colors[i] + 1) % 3
            if colors[i] == 2:
                blue += 1
            elif colors[i] == 0:
                blue -= 1

        if blue > maxBlue:
            maxBlue = blue

    return maxBlue


runtests(lamps)
