from egzP3atesty import runtests
from math import inf


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


def wybory(T):
    m = len(T)
    result = 0

    for head in T:
        dp = [[0, [-1 for _ in range(m)]] for _ in range(head.fundusze + 1)]
        curr = head
        while curr is not None:
            for i in range(curr.koszt, curr.fundusze + 1):
                dp[i] = max(curr.wyborcy, dp[i])
            curr = curr.next

        for i in range(head.fundusze + 1):
            curr = head
            while curr is not None:
                if i - curr.koszt >= 0:
                    dp[i] = max(dp[i], dp[i - curr.koszt] + curr.wyborcy)
                curr = curr.next

            print(dp)
        result += max(dp)

    return result


runtests(wybory, all_tests=False)
