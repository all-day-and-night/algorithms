import math


def solution(n):
    answer = 0

    if n == int(math.sqrt(n)) ** 2:
        return int(math.sqrt(n) + 1) ** 2
    return -1