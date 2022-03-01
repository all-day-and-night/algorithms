"""
1이 더 빠름

heapq 말고도 더 빠른 방법이 있다
"""

from heapq import heappop, heappush, heapify


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    i, j = 0, 0

    while i < N and j < N:
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1

        else:
            j += 1

    return answer


def solution2(A, B):
    answer = 0
    a = [i for i in A]
    b = [i for i in B]

    heapify(a)
    heapify(b)
    while a and b:
        if a[0] < b[0]:
            heappop(a)
            heappop(b)
            answer += 1
        else:
            heappop(b)
    return answer