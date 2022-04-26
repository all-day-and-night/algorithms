from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0


def bfs(x, y, check):
    key = board[x][y]

    q = deque()
    q.append([x, y])
    rainbows = []
    normals = []
    normals.append([x, y])
    check[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                continue

            if board[nx][ny] < 0:
                continue

            if check[nx][ny] == 1:
                continue

            if board[nx][ny] == key:
                q.append([nx, ny])
                check[nx][ny] = 1
                normals.append([nx, ny])

            elif board[nx][ny] == 0:
                q.append([nx, ny])
                check[nx][ny] = 1
                rainbows.append([nx, ny])

    for k, l in rainbows:
        check[k][l] = 0

    return len(normals) + len(rainbows), len(rainbows), normals + rainbows


def delete(arr):
    for x, y in arr:
        board[x][y] = -2


def gravity():
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < N and board[r + 1][j] == -2:
                        board[r + 1][j] = board[r][j]
                        board[r][j] = -2
                        r += 1
                    else:
                        break


def rotate():
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[N - 1 - j][i] = board[i][j]

    for i in range(N):
        for j in range(N):
            board[i][j] = new[i][j]


answer = 0

while True:

    check = [[0] * N for _ in range(N)]

    max_ = 0
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] < 1:
                continue

            if not check[i][j]:
                temp = bfs(i, j, check)
                if temp[0] > 1:
                    blocks.append(temp)

    if len(blocks) == 0:
        break

    blocks.sort(reverse=True)
    answer += blocks[0][0] ** 2
    delete(blocks[0][2])

    gravity()
    rotate()
    gravity()


print(answer)
