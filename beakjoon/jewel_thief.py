from collections import deque
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N, K = map(int, input().split())


data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append([a, b])

packs = []
for _ in range(K):
    a = int(input())
    packs.append(a)

data.sort(key=lambda x: x[0])
packs.sort()

data = deque(data)
packs = deque(packs)
temp = []

answer = []

while packs:
    while data and data[0][0] <= packs[0]:
        m, v = data.popleft()
        heappush(temp, (-1) * v)

    if temp:
        answer.append(heappop(temp) * (-1))
    packs.popleft()


print(sum(answer))