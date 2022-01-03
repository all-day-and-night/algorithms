import sys
sys.setrecursionlimit(10**9)

V = int(input())

def dfs(a, parent, graph):
    for g in graph[a]:
        if parent[g] == 0:
            parent[g] = a
            dfs(g, parent, graph)


graph = [[] for _ in range(V+1)]
parent = [0] * (V+1)
parent[1] = 1

for i in range(V-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, parent, graph)

for p in parent[2:]:
    print(p)