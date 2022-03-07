import math


def isPrime(value):
    for i in range(2, int(math.sqrt(value) + 1)):
        if value % i == 0:
            return False

    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if isPrime(i):
            answer += 1

    return answer