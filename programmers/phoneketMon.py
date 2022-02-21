"""
brute force로 굳이 하나씩 계산 안해도 풀리는 문제
그냥 풀지 말고 고민 좀 하고 풀자
너무 급하게 풀려고 하니까 틀리는 거야
"""

from itertools import combinations


def solution(nums):
    answer = 0
    len_ = len(nums)
    nums = list(set(nums))

    if len_ // 2 >= len(nums):
        return len(nums)

    else:
        return len_ // 2



