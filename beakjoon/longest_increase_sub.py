"""
가장 긴 증가하는 부분수열

문제는 시간 복잡도를 낮추는 것

이분탐색을 통해 들어갈 위치를 찾고 수행

"""

import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

arr = [0]

for d in data:
    if arr[-1] < d:
        arr.append(d)

    else:
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < d:
                left = mid + 1
            else:
                right = mid
        arr[right] = d

print(len(arr) - 1)
