import sys

input = sys.stdin.readline


def binary_search(key, data):
    left = 0
    right = len(data) - 1

    answer = -1
    while left <= right:
        mid = (left + right) // 2

        if data[mid] == key:
            return True
        elif data[mid] < key:
            left = mid + 1
        elif data[mid] > key:
            right = mid - 1

    return False


N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

"""a = set(a)

answer = []
for key in b:
    if key in a:
        answer.append(1)
    else:
        answer.append(0)
"""
a.sort()
answer = []
for key in b:
    if binary_search(key, a):
        answer.append(1)
    else:
        answer.append(0)

for ans in answer:
    print(ans, end=' ')





