def sol(value, n):
    result = ""
    while value:
        temp = value % 2

        if temp == 0:
            result += ' '
        else:
            result += '#'

        value = value // 2

    while len(result) < n:
        result += ' '

    return result[::-1]


def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer.append(sol(a | b, n))
    return answer