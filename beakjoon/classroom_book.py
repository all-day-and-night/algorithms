"""
"""


from heapq import heappush, heappop

N = int(input())


data = []

for _ in range(N):
    start, end = map(int, input().split())
    data.append([start, end])

data.sort()

q = []

heappush(q, data[0][1])

for i in range(1, N):
    if data[i][0] < q[0]:
        heappush(q, data[i][1])
    else:
        heappop(q)
        heappush(q, data[i][1])

print(len(q))
