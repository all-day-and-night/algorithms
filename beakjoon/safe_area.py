from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j, h, check, N):
    q = deque()
    q.append([i, j])
    check[i][j] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                continue

            if check[nx][ny] == 1:
                continue

            if board[nx][ny] >= h:
                check[nx][ny] = 1
                q.append([nx, ny])



N = int(input())

board = []

max_h = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for t in temp:
        max_h = max(max_h, t)
    board.append(temp)

answer = 0

for h in range(1, max_h + 2):
    check = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] >= h and not check[i][j]:
                bfs(i, j, h, check, N)
                cnt += 1

    answer = max(answer, cnt)

print(answer)


