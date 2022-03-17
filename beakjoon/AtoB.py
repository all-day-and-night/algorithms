from collections import deque
from heapq import heappush, heappop

A, B = map(int, input().split())


def sol(A, B):

    q = []

    heappush(q, [1, A])

    while q:
        cnt, now = heappop(q)

        if now == B:
            return cnt

        for nxt in [now * 2, now * 10 + 1]:
            if nxt < B:
                heappush(q, [cnt + 1, nxt])
            elif nxt == B:
                return cnt + 1
    return -1

print(sol(A, B))
