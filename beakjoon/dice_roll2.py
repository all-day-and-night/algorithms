from collections import deque



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def roll_up(dice):
    temp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp


def roll_down(dice):
    temp = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = temp


def roll_right(dice):
    temp = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = temp


def roll_left(dice):
    temp = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = temp

def print_dice(dice):
    print("   %d    " % dice[1])
    print("%d  %d  %d" % (dice[3], dice[0], dice[2]))
    print("   %d    " % dice[4])
    print("   %d    " % dice[5])


def bfs(board, x, y, check, N, M):
    q = deque()

    q.append([x, y])
    key = board[x][y]
    check[x][y] = 1
    cnt = 0

    road = []

    while q:
        x, y = q.popleft()
        road.append([x, y])
        cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if board[nx][ny] == key and check[nx][ny] == 0:
                q.append([nx, ny])
                check[nx][ny] = 1

    score = key * cnt

    for i, j in road:
        check[i][j] = score

    return

T = int(input())

for _ in range(T):
    dice = [1, 2, 3, 4, 5, 6]
    N, M, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    x, y = 0, 0
    dir_ = 0
    check = [[0] * N for _ in range(M)]
    answer = 0
    for _ in range(K):
        nx, ny = x + dx[dir_], y + dy[dir_]

        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            dir_ = (dir_ + 2) % 4
            nx, ny = x + dx[dir_], y + dy[dir_]

        x, y = nx, ny

        if dir_ == 0:
            roll_right(dice)
        elif dir_ == 1:
            roll_down(dice)
        elif dir_ == 2:
            roll_left(dice)
        elif dir_ == 3:
            roll_up(dice)

        check = [[0] * M for _ in range(N)]
        if check[x][y] == 0:
            bfs(board, x, y, check, N, M)
            answer += check[x][y]
        else:
            answer += check[x][y]


        #방향 바꾸기
        a, b = dice[-1], board[x][y]
        if a > b:
            dir_ = (dir_ + 1) % 4
        elif a < b:
            dir_ = (dir_ - 1) % 4

    print("#%d %d"%(T+1, answer))


"""
3
4 5 1
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 2
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
4 5 3
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5

"""