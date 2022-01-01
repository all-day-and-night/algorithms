V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]
check = [0] * (V+1)
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

now = 1

q = []
q.append(now)
while q:
    now = q.pop()
    check[now] = 1
    for g in graph[now]:
        if check[g] == 0:
            q.append(g)

result = check.count(1)

print(result - 1)