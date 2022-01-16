import math


def hexTo(n, k):
    temp = []
    while n > 0:
        temp.append(n % k)
        n = n // k
    temp = temp[::-1]
    result = ""
    for t in temp:
        result += str(t)
    return result


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if n % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(n, k):
    answer = 0
    result = hexTo(n, k).split('0')
    for r in result:
        if r and r != '1' and isPrime(int(r)):
            answer += 1

    return answer