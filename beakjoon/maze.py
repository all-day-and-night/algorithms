from collections import deque

N, M = map(int, input().split())
INF = int(1e9)


board = []
for _ in range(N):
    board.append(list(input()))

distance = [[INF] * M for _ in range(N)]

x, y = 0, 0
q = deque()
q.append([x, y, 1])
distance[0][0] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y, dist = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            continue

        if board[nx][ny] == '1':
            if distance[nx][ny] > dist + 1:
                distance[nx][ny] = dist + 1
                q.append([nx, ny, dist + 1])

print(distance[N-1][M-1])