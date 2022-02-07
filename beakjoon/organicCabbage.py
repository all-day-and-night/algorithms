"""
dfs, bfs로 풀 수 있지만
set으로 풀수있는 방법이 있을 것이라 생각해서 사용해봄
굳이? 라는 생각도 좀 들긴 했는데
좋은시도일듯
나중에 union find도 이런식으로 문제를 해결해보자
"""

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(idx, cabbages, N, M):
    q = deque()
    x, y = idx // M, idx % M
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if nx * M + ny in cabbages:
                cabbages.remove(nx * M + ny)
                q.append((nx, ny))
    return


N = int(input())

result = []
for _ in range(N):
    M, N, K = map(int, input().split())

    cabbages = set()
    for _ in range(K):
        y, x = map(int, input().split())
        cabbages.add(x * M + y)

    answer = 0
    while cabbages:
        answer += 1
        idx = cabbages.pop()
        bfs(idx, cabbages, N, M)

    result.append(answer)

for re in result:
    print(re)


"""
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, cabbages, N, M):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if cabbages[nx][ny] == 1:
                cabbages[nx][ny] = 0
                q.append((nx, ny))
    return


N = int(input())

result = []
for _ in range(N):
    M, N, K = map(int, input().split())

    cabbages = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        cabbages[x][y] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if cabbages[i][j] == 1:
                cabbages[i][j] = 0
                bfs(i, j, cabbages, N, M)
                answer += 1

    result.append(answer)

for re in result:
    print(re)
"""


"""
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
"""