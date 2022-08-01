"""
meet in the middle

2^20이 넘어갈 경우 시간초과에 걸릴 수 있다.


"""

import sys
from itertools import combinations

input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

arr1 = arr[:N//2]
arr2 = arr[N//2:]

sub1 = [0]
sub2 = [0]

for i in range(1, len(arr1) + 1):
    for sub in combinations(arr1, i):
        sub1.append(sum(sub))

sub1.sort()

for i in range(1, len(arr2) + 1):
    for sub in combinations(arr2, i):
        sub2.append(sum(sub))

answer = 0

for sub in sub2:
    if sub > C:
        continue

    left = 0
    right = len(sub1)

    while left < right:
        mid = (left + right) // 2

        if sub1[mid] + sub > C:
            right = mid
        else:
            left = mid + 1

    answer += right

print(answer)
