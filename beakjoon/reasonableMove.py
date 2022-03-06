"""
가장 처음 다익스트라 알고리즘을 사용하여 각 노드에서 목적지까지 최단경로를 찾아야 한다.

이후 각 노드에서 다른 노드로 넘어갈 때 최단경로를 비교하여 최단경로가 감소하는 상황이면 움직인다.

합리적인 이동경로를 구할 때 bfs로 구하려 하였지만 문제는 메모리 초과가 발생하는 것이었다.

dfs와 메모이 제이션을 사용하여 문제를 해결할 수 있었다.

"""

from collections import deque
import heapq

N, M = map(int, input().split())


graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)
S, T = 1, 2
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

q = []
heapq.heappush(q, [0, T])
distance[T] = 0
while q:
    dist, now = heapq.heappop(q)

    for g, cost in graph[now]:
        if distance[g] > dist + cost:
            distance[g] = dist + cost
            heapq.heappush(q, [dist + cost, g])

q = deque()
q.append(S)
cnt = 0

dp = [-1] * (N+1)

def dfs(now):
    if dp[now] != -1:
        return dp[now]
    if now == 2:
        dp[now] = 1
        return dp[now]
    dp[now] = 0
    for g, cost in graph[now]:
        if distance[g] < distance[now]:
            dp[now] += dfs(g)

    return dp[now]

print(dfs(1))

