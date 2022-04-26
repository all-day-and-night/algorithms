N, K = map(int, input().split())

board = []
chess = [[[] for _ in range(N)] for _ in range(N)]
horse = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for _ in range(N):
    board.append(list(map(int, input().split())))


for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1] = [i]


def change_dir(dir):
    if dir in [0, 2]:
        return dir + 1
    else:
        return dir - 1


def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]

    # 막히거나 파란색일때
    if nx < 0 or ny < 0 or nx > N-1 or ny > N-1 or board[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1 or board[nx][ny] == 2:
            return True

    horse_up = []

    for h_idx, h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y] = chess[x][y][:h_idx]
            break

    #빨간색
    if board[nx][ny] == 1:
        horse_up = horse_up[::-1]

    for h in horse_up:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)

    if len(chess[nx][ny]) > 3:
        return False

    return True




T = 0

while T < 1000:

    is_end = False
    for i in range(K):
        if not solve(i):
            is_end = True
            break
    T += 1

    if is_end:
        print(T)
        break

if T > 999:
    print(-1)






