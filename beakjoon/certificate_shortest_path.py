from heapq import heappush, heappop

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

v1, v2 = map(int, input().split())

q = []
INF = int(1e9)
distance1 = [INF] * (N+1)
distance1[1] = 0
heappush(q, [1, 0])

while q:
    now, dist = heappop(q)

    for g, cost in graph[now]:
        if distance1[g] > dist + cost:
            distance1[g] = dist + cost
            heappush(q, [g, dist + cost])

distance2 = [INF] * (N+1)
distance2[N] = 0
q = []
heappush(q, [N, 0])

while q:
    now, dist = heappop(q)

    for g, cost in graph[now]:
        if distance2[g] > dist + cost:
            distance2[g] = dist + cost
            heappush(q, [g, dist + cost])


distance3 = [INF] * (N+1)
distance3[v1] = 0
q = []
heappush(q, [v1, 0])

while q:
    now, dist = heappop(q)

    for g, cost in graph[now]:
        if distance3[g] > dist + cost:
            distance3[g] = dist + cost
            heappush(q, [g, dist + cost])

ans1 = distance1[v1] + distance2[v2] + distance3[v2]
ans2 = distance1[v2] + distance2[v1] + distance3[v2]

answer = min(ans1, ans2)
if answer >= INF:
    print(-1)
else:
    print(answer)