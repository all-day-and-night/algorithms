def check(value):
    result = 1
    for i in range(2, value + 1):
        if value % i == 0:
            result += 1

    return result


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if check(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer