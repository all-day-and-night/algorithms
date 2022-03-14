"""
트리의 가장 긴 지름은

루트 노드에서 가장 먼 노드를 찾고

그 노드에서 가장 긴 노드를 찾는 것

기억해두자
"""

import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


N = int(input())

def dfs(root, w):
    for g, cost in graph[root]:
        if distance[g] == -1:
            distance[g] = w + cost
            dfs(g, w + cost)
    return



graph = [[] for _ in range(N+1)]

for _ in range(N - 1):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

distance = [-1] * (N+1)

dfs(1, 0)

max_idx = distance.index(max(distance))
distance = [-1] * (N+1)
distance[max_idx] = 0

dfs(max_idx, 0)

print(distance[distance.index(max(distance))])