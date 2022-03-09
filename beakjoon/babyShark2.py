"""
거의 반년 이상만에 푼 문제

그 때는 답지가 없으면 못 풀 문제였지만

이제는 많이 성장한거 같다

해보자!
"""

from collections import deque

def get_dist(x, y, nx, ny):
    return max(abs(nx - x), abs(ny - y))

N, M = map(int, input().split())

mat = []

sharks = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            sharks.append([i, j])

    mat.append(temp)

answer = 0

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

for shark in sharks:
    x, y = shark
    q = deque()

    q.append([x, y, 1])
    while q:
        x, y, dist = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if mat[nx][ny] == 1:
                continue

            if mat[nx][ny] != 0 and mat[nx][ny] <= dist + 1:
                continue

            mat[nx][ny] = dist + 1
            q.append([nx, ny, dist + 1])

answer = 0
for m in mat:
    answer = max(answer, max(m))
print(answer-1)





