def toHex(num):
    values = str(num)

    result = 0
    for i in range(len(values)):
        result += int(values[-1 - i]) * 3 ** i

    return result


def toTri(num):
    value = num
    result = ""
    while value > 0:
        result += str(value % 3)
        value = value // 3

    return int(result)


def solution(n):
    return toHex(toTri(n))
