import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

def dfs(root):
    check[root] = 1
    for g in graph[root]:
        if check[g] == 0:
            dfs(g)
            check[root] += check[g]
    return

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(R)


for i in range(Q):
    print(check[int(input())])




