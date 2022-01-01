def bfs(board, x, y, check, N):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = []
    q.append([x, y])
    check[x][y] = 1
    cnt = 0
    while q:
        x, y = q.pop()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '1' and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append([nx, ny])
    return cnt


N = int(input())

board = []
for _ in range(N):
    board.append(list(input()))

total = 0
result = []

check = [[0] * N for _ in range(N)]



for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and check[i][j] == 0:
            cnt = bfs(board, i, j, check, N)
            if cnt > 0:
                total += 1
                result.append(cnt)

result.sort()

print(total)
for r in result:
    print(r)