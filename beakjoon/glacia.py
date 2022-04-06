from collections import deque
from copy import deepcopy

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def melt(board, N, M):
    temp = deepcopy(board)

    ismelt = False
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if x < 0 or x > N-1 or y < 0 or y > M-1:
                        continue
                    if board[x][y] == 0:
                        cnt += 1
                temp[i][j] = board[i][j] - cnt

                if temp[i][j] < 0:
                    temp[i][j] = 0

                ismelt = True

    return temp, ismelt

def dfs(x, y, check, board, N, M):
    q = deque()
    q.append([x, y])
    check[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            if board[nx][ny] != 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append([nx, ny])

    return 1


time = 0
while True:
    time += 1
    board, ismelt = melt(board, N, M)

    if not ismelt:
        print(0)
        break

    check = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and check[i][j] == 0:
                cnt += dfs(i, j, check, board, N, M)

    if cnt > 1:
        print(time)
        break

