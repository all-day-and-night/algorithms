from collections import deque

V, E = map(int, input().split())


graph = [[] for _ in range(V)]
indegree = [0] * V
for _ in range(E):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

q = deque()

for i in range(V):
    if indegree[i] == 0:
        q.append(i)


result = []
while q:
    now = q.popleft()
    result.append(now)
    for g in graph[now]:
        indegree[g] -= 1
        if indegree[g] == 0:
            q.append(g)

for r in result:
    print(r + 1, end=' ')