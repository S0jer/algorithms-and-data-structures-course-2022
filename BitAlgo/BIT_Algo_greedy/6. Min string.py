# Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować algorytm, który usunie ze stringa
# duplikaty tak, że otrzymany string będzie leksykograficznie najmniejszy.
# Przykład: cbacdcbc, odpowiedzią jest acdb.
#
# Wskazówka:
# ord(“a”) = 97; ord(“b”) = 98; ... ; ord(“z”) = 122


from collections import deque


def minString(S):
    mm = 65
    lettersCount = [0 for _ in range(59)]
    visited = [False for _ in range(59)]

    for s in S:
        lettersCount[ord(s) - mm] += 1

    Q = deque()

    for s in S:
        idx = ord(s) - mm
        lettersCount[idx] -= 1

        if not visited[idx]:
            while len(Q) > 0 and s < Q[-1] and lettersCount[ord(Q[-1]) - mm] > 0:
                visited[ord(Q[-1]) - mm] = False
                Q.pop()

            visited[idx] = True
            Q.append(s)

    result = ""
    while len(Q) > 0:
        result += Q.popleft()

    return result


r = "cbacdcbc"

print(minString(r))
