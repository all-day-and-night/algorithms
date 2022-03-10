from collections import deque

N, M = map(int, input().split())

max_ = 100001

INF = int(1e9)
data = [INF for _ in range(max_)]

q = deque()
q.append(N)
data[N] = 0

while q:
    now = q.popleft()

    for nxt in [now + 1, now - 1]:
        if nxt < 0 or nxt > max_-1:
            continue
        if data[nxt] > data[now] + 1:
            data[nxt] = data[now] + 1
            q.append(nxt)

    nxt = now * 2
    if nxt < 0 or nxt > max_-1:
        continue
    if data[nxt] > data[now]:
        data[nxt] = data[now]
        q.append(nxt)
        continue

print(data[M])

