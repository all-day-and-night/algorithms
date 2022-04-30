from copy import deepcopy
from collections import deque

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sx = {'1': -1, '2': 0, '3': 1, '4': 0}
sy = {'1': 0, '2': -1, '3': 0, '4': 1}

dfs_result = []
max_ = -1
check = [[0] * 4 for _ in range(4)]


def dfs(x, y, cnt, path):
    global max_, dfs_result

    if len(path) == 3:
        if cnt > max_:
            max_ = cnt
            dfs_result = [[cnt, int(path)]]


        return

    for dir_, l in enumerate([[-1, 0], [0, -1], [1, 0], [0, 1]]):
        nx, ny = x + l[0], y + l[1]

        if nx < 0 or ny < 0 or nx > 3 or ny > 3:
            continue

        if check[nx][ny] == 0:

            check[nx][ny] = 1
            dfs(nx, ny, cnt + len(board[nx][ny]), path + str(dir_ + 1))
            check[nx][ny] = 0

        else:
            dfs(nx, ny, cnt, path + str(dir_ + 1))

    return


board = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
shark = [[0] * 4 for _ in range(4)]
temp_board = [[[] for _ in range(4)] for _ in range(4)]

M, S = map(int, input().split())

fish = []

for _ in range(M):
    x, y, c = map(int, input().split())
    board[x-1][y-1].append(c-1)

shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1

for _ in range(S):

    temp_board = [[[] for _ in range(4)] for _ in range(4)]
    fish = []
    #복제
    for i in range(4):
        for j in range(4):
            for c in board[i][j]:
                fish.append([i, j, c])

    for i in range(4):
        for j in range(4):

            while board[i][j]:
                c = board[i][j].pop()

                nx, ny = -1, -1
                flag = False
                for _ in range(8):
                    tx, ty = i + dx[c], j + dy[c]
                    if tx < 0 or ty < 0 or tx > 3 or ty > 3:
                        c = (c - 1) % 8
                        continue

                    if tx == shark_x and ty == shark_y:
                        c = (c - 1) % 8
                        continue

                    if smell[tx][ty] != 0:
                        c = (c - 1) % 8
                        continue

                    nx, ny = tx, ty
                    flag = True
                    break

                if not flag:
                    nx, ny = i, j

                temp_board[nx][ny].append(c)

    for i in range(4):
        for j in range(4):
            while temp_board[i][j]:
                board[i][j].append(temp_board[i][j].pop())

    # 상어 움직이기 bfs?
    check = [[0] * 4 for _ in range(4)]
    dfs_result = []
    max_ = -1
    dfs(shark_x, shark_y, 0, "")
    nxt_path = dfs_result[0][1]

    path = list(str(nxt_path))
    for p in path:
        nx, ny = shark_x + sx[p], shark_y + sy[p]
        if len(board[nx][ny]) > 0:
            smell[nx][ny] = 3
        board[nx][ny] = []
        shark_x, shark_y = nx, ny

    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1


    # 복제

    for f in fish:
        board[f[0]][f[1]].append(f[2])


answer = 0
for i in range(4):
    for j in range(4):
        answer += len(board[i][j])


print(answer)





