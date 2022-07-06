from zad1testy import runtests



def intuse(I, x, y):
    n = len(I)

    nums = []  # tablica wszystkich cyfr wystepujacych w przedzialach
    for i in range(n):
        nums.append(I[i][0])
        nums.append(I[i][1])

    nums.sort()
    uniquenums = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        uniquenums.append(nums[i])

    m = max(max(nums), len(nums))
    DPY = [False for _ in range(m + 1)]  # True if current num can be connected with Y
    DPX = [False for _ in range(m + 1)]  # True if current num can be connected with X

    DPY[y] = True
    DPX[x] = True

    intervals_sorted_reversed = sorted(I, reverse=True)

    for interval in intervals_sorted_reversed:
        if DPY[interval[1]] == True:
            DPY[interval[0]] = True

    intervals_sorted = sorted(I, key=lambda x: x[1])

    for interval in intervals_sorted:
        if DPX[interval[0]] == True:
            DPX[interval[1]] = True

    result = []
    for i in range(len(I)):
        if DPX[I[i][0]] and DPY[I[i][1]]:
            result.append(i)

    return result


runtests(intuse)
