import sys
from collections import deque
sys.setrecursionlimit(10**6)
def dfs(graph, start, check, N, depth):
    if depth == N+1:
        return

    if check[start] == 0:
        check[start] = 1
        print(start, end=' ')

    for g in graph[start]:
        if check[g] == 0:
            dfs(graph, g, check, N, depth+1)
    return


def bfs(graph, start, check):

    q = deque()
    q.append(start)
    check[start] = 1

    while q:
        now = q.popleft()
        print(now, end=' ')
        for g in graph[now]:
            if check[g] == 0:
                q.append(g)
                check[g] = 1



N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

check = [0] * (N+1)

dfs(graph, V, check, N, 0)
check = [0] * (N+1)
print()
bfs(graph, V, check)


