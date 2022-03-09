import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    visited[now] = 1
    dp[now][0] = 1
    for g in graph[now]:
        if not visited[g]:
            dfs(g)
            dp[now][0] += min(dp[g][0], dp[g][1])
            dp[now][1] += dp[g][0]

dfs(1)
print(min(dp[1]))
