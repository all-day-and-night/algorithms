

N = int(input())

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

row = 101
col = 101

check = [[0] * 101 for _ in range(101)]
for _ in range(N):
    y, x, d, g = map(int, input().split())

    check[x][y] = 1
    move = [d]

    nx, ny = x + dx[d], y + dy[d]

    check[nx][ny] = 1

    for i in range(g):

        size = len(move)
        for j in range(size-1, -1, -1):
            dir_ = (move[j] + 1) % 4
            nx, ny = nx + dx[dir_], ny + dy[dir_]
            if nx < 0 or ny < 0 or ny > row-1 or nx > col-1:
                continue

            check[nx][ny] = 1
            move.append(dir_)


cnt = 0
for i in range(row-1):
    for j in range(col-1):
        if check[i][j] == 1:
            if check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
                cnt += 1
print(cnt)
