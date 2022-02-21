"""
처음에 문제를 풀 때 모든 노드에서 가장 긴 거리를 가진 노드를 찾아 비교해서 문제를 풀었다

하지만 아래 링크에 보면 아무 노드에서 가장 긴 거리를 가진 노드를 찾고

가장 긴 거리를 가진 노드에서 다시 가장 긴 노드의 거리가 정답이었다.

https://blog.myungwoo.kr/112

"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    temp = list(map(int, input().split()))

    a = temp[0]
    nexts = temp[1:-1]
    for i in range(0, len(nexts), 2):
        graph[a].append([nexts[i], nexts[i+1]])


INF = int(1e9)
def bfs(start):

    visit = [INF] * (N+1)

    q = deque()
    q.append([start, 0])
    visit[start] = 0

    max_ = [0, 0]
    while q:
        now, dist = q.popleft()
        for g, cost in graph[now]:
            if visit[g] > dist + cost:
                q.append([g, dist+cost])
                visit[g] = dist + cost
                if max_[0] < visit[g]:
                    max_[0] = visit[g]
                    max_[1] = g

    return max_

dist, node = bfs(1)
dist, node = bfs(node)

print(dist)

