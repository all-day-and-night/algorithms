from heapq import heappush, heappop

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e9)

distance = [INF] * 200001
end = len(distance)

q = []
heappush(q, [0, N])
distance[N] = 0

while q:
    dist, now = heappop(q)
    if now == M:
        break
    for i in [now - 1, now + 1, now * 2]:

        if i < 0 or i > end-1:
            continue

        if distance[i] > dist + 1:
            distance[i] = dist + 1
            heappush(q, [dist + 1, i])

print(distance[M])