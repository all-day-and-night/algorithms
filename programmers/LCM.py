import math
from collections import defaultdict


def gcd(a, b):
    result = 0
    for i in range(100, 0, -1):
        if a % i == 0 and b % i == 0:
            result = i
            break
    return result


def solution(arr):
    answer = arr[0]
    for a in arr:
        answer = answer * a // gcd(answer, a)

    return answer