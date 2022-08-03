import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
N = int(input())

nums = []



for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str, comb))))

nums.sort()

if N >= len(nums):
    print(-1)
else:
    print(nums[N])
