import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())

nums = [0] + list(map(int, input().split()))

def dfs(now):
    visited[now] = 1
    for nxt in graph[now]:
        if visited[nxt] == 0:
            dfs(nxt)
            dp[now][1] += dp[nxt][0]
            dp[now][0] += max(dp[nxt][1], dp[nxt][0])

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dp = [[0, nums[i]] for i in range(N+1)]
visited = [0] * (N+1)

dfs(1)

print(max(dp[1]))

