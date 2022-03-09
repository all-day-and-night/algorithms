import heapq

V, E = map(int, input().split())

graph = [[] for _ in range(V)]

indegree = [0] * V

for _ in range(E):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1


q = []

for i, v in enumerate(indegree):
    if v == 0:
        heapq.heappush(q, i)

answer = []
while q:
    now = heapq.heappop(q)
    answer.append(now)
    for g in graph[now]:
        indegree[g] -= 1
        if indegree[g] == 0:
            heapq.heappush(q, g)



for ans in answer:
    print(ans + 1, end=' ')


