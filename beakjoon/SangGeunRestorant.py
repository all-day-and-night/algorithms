import heapq
import sys

input = sys.stdin.readline

N = int(input())

data = []

for _ in range(N):
    a, b = map(int, input().split())

    data.append([a, b])

data.sort(key=lambda x: x[1])

INF = 9876543210987654321
ans = [INF] * N

victims = [0] * N

victims[-1] = data[-1][0]
for i in range(N - 2, -1, -1):
    victims[i] = min(victims[i + 1], data[i][0])

now = 0
for i in range(N):
    ans[i] = min(ans[i], now + victims[i])
    now += data[i][1]

q = []
now = 0

for i in range(N):
    now += data[i][1]
    heapq.heappush(q, data[i][0] - data[i][1])
    ans[i] = min(ans[i], now + q[0])

for i in ans:
    print(i)


