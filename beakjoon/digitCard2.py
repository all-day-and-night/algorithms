from bisect import bisect_left, bisect_right
from collections import Counter

def bisectLeft(data, value):
    left = 0
    right = len(data) - 1
    mid = 0
    answer = -1
    while left <= right:
        mid = (left + right) // 2

        if data[mid] >= value:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer


def bisectRight(data, value):
    left = 0
    right = len(data) - 1
    mid = 0
    answer = -1
    while left <= right:
        mid = (left + right) // 2

        if data[mid] <= value:
            answer = mid + 1
            left = mid + 1

        else:
            right = mid - 1

    return answer



def calcRange(data, value):
    left = bisect_left(data, value)
    right = bisect_right(data, value)
    #print(value, left, right)
    return right - left


def madeRange(data, value):
    left = bisectLeft(data, value)
    right = bisectRight(data, value)
    #print(value, left, right)
    return right - left



N = int(input())

data = list(map(int, input().split()))

M = int(input())

data2 = list(map(int, input().split()))

data.sort()
"""
for value in data2:
    print(madeRange(data, value), end=' ')
    """
counter = Counter(data)

for value in data2:
    if value in counter.keys():
        print(counter[value], end=' ')
    else:
        print(0, end=' ')
