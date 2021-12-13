"""
효율성을 고려해야하는 문제였다.
heapq를 사용하면 효율성 문제를 해결할 수 있다.
"""

import heapq


def solution(n, works):
    answer = 0
    q = []

    for work in works:
        heapq.heappush(q, [-work, work])

    while n > 0:
        work = heapq.heappop(q)[1] - 1
        heapq.heappush(q, [-work, work])
        n -= 1

    for item in q:
        if item[1] > 0:
            answer += item[1] ** 2

    return answer