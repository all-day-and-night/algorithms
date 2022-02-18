from itertools import combinations
import math


def prime():
    answer = [False] * 3001
    for i in range(2, 3001):
        isPrime = True
        for x in range(2, int(math.sqrt(i)) + 1):
            if i % x == 0:
                isPrime = False
                break
        if isPrime:
            answer[i] = True
    return answer


def solution(nums):
    answer = 0
    primes = prime()
    for cand in combinations(nums, 3):
        if primes[sum(cand)]:
            answer += 1

    return answer