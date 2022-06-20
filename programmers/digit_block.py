import math


def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
            continue

        sqrt = int(math.sqrt(i))

        for j in range(2, sqrt + 1):
            mok = i // j

            if mok > 10 ** 7:
                continue

            if i % j == 0:
                result.append(mok)
                break
        else:
            result.append(1)

    return result