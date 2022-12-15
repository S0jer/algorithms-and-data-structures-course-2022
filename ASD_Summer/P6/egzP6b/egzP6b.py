from egzP6btesty import runtests


def jump(M):
    n = len(M)
    position = [0, 0]
    moves = {
        "UL": (-1, 2),
        "UR": (1, 2),
        "RU": (2, 1),
        "RD": (2, -1),
        "DR": (1, -2),
        "DL": (-1, -2),
        "LD": (-2, -1),
        "LU": (-2, 1)
    }
    movesHistory = {
        (0, 0): True
    }
    result = 1
    for i in range(n):
        m = moves.get(M[i])
        position = (position[0] + m[0], position[1] + m[1])

        if movesHistory.get(position):
            movesHistory[position] = False
            result -= 1
        else:
            movesHistory[position] = True
            result += 1

    return result


runtests(jump, all_tests=True)
