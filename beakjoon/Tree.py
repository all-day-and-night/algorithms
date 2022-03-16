"""
단순히 트리구조를 확인하는 것이면 데이터 양이 많을 때 union find를 사용하지 않아도 괜찮다

bfs를 사용하여 방문한 노드를 한번 더 방문한다면 사이클이 생기므로 트리로 계산하지 않는다


"""

from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def bfs(x):
    isTrue = True
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        if visited[now] == 1:
            isTrue = False
        visited[now] = 1
        for nxt in graph[now]:
            if visited[nxt] == 0:
                q.append(nxt)

    return isTrue


times = 1
while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    graph = [[] for _ in range(N+1)]
    visited = [0 for i in range(0, N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 1:
            continue
        if bfs(i):
           cnt += 1

    answer = ""
    if cnt == 0:
        answer = "No trees."
    elif cnt == 1:
        answer = "There is one tree."
    else:
        answer = "A forest of %d trees." % cnt

    print("Case %d: " % times + answer)
    times += 1