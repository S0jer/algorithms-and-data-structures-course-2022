from zad2testy import runtests

from queue import PriorityQueue


def robot(L, A, B):
    n, m = len(L), len(L[0])
    dp = [[[[-1 for a in range(3)]
            for b in range(4)]
           for c in range(m)]
          for d in range(n)]

    Q = PriorityQueue()

    Q.put((0, A[1], A[0], 0, 0))

    costs = [60, 40, 30]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while not Q.empty():
        result, x, y, m_id, cost_id = Q.get()

        if (y, x) == B:
            return result
        if dp[x][y][m_id][cost_id] != -1:
            continue
        dp[x][y][m_id][cost_id] = result

        Q.put((result + 45, x, y, (m_id + 1) % 4, 0))
        Q.put((result + 45, x, y, (m_id + 3) % 4, 0))

        x += moves[m_id][0]
        y += moves[m_id][1]

        if L[x][y] == 'X':
            continue

        Q.put((result + costs[cost_id], x, y, m_id, min(cost_id + 1, 2)))


runtests(robot)
