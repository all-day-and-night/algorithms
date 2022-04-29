
kx = {1: 0, 2: 0, 3: -1, 4: 1}
ky = {1: 1, 2: -1, 3: 0, 4: 0}



def dfs(x, y, c, depth, N, M):
    if depth == 0 or visited[x][y] != 0:
        return

    if x < 0 or y < 0 or x > N-1 or y > M-1:
        return

    new[x*2][y*2] += depth
    visited[x][y] = 1
    nxt = []
    if c == 1:
        nxt = [[x-1, y+1], [x, y+1], [x+1, y+1]]
    elif c == 2:
        nxt = [[x-1, y-1], [x, y-1], [x+1, y-1]]
    elif c == 3:
        nxt = [[x-1, y-1], [x-1, y], [x-1, y+1]]
    elif c == 4:
        nxt = [[x+1, y-1], [x+1, y], [x+1, y+1]]
    for nx, ny in nxt:
        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            continue

        x2 = x * 2
        y2 = y * 2

        nx2 = nx * 2
        ny2 = ny * 2
        if x2 == nx2 or y2 == ny2:
            if new[(x2 + nx2) // 2][(y2 + ny2) // 2] == 0:
                dfs(nx, ny, c, depth-1, N, M)
                continue
            continue

        if c < 3:
            if new[(x2 + nx2) // 2][y2] == 0 and new[nx2][(y2 + ny2) // 2] == 0:
                dfs(nx, ny, c, depth-1, N, M)
        else:
            if new[x2][(y2 + ny2) // 2] == 0 and new[(x2 + nx2) // 2][ny2] == 0:
                dfs(nx, ny, c, depth - 1, N, M)




def temp_avg(x, y):
    visited[x][y] = 1
    for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:

        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            continue

        if visited[nx][ny] != 0:
            continue

        x2 = x * 2
        y2 = y * 2
        nx2 = nx * 2
        ny2 = ny * 2

        if new[(x2 + nx2) // 2][(y2 + ny2) // 2] != 0:
            continue

        gap = abs(new[x2][y2] - new[nx2][ny2]) // 4
        if new[x2][y2] > new[nx2][ny2]:
            tmp_board[x][y] -= gap
            tmp_board[nx][ny] += gap

        elif new[x2][y2] < new[nx2][ny2]:
            tmp_board[x][y] += gap
            tmp_board[nx][ny] -= gap

board = []
heats = []
check = []
temp_board = []
visited = []
tmp_board = []

loop = int(input())

for test_case in range(loop):
    N, M, K = map(int, input().split())

    board = []
    heats = []
    check = []
    temp_board = []
    visited = []
    tmp_board = []

    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            if temp[j] > 0:
                if temp[j] == 5:
                    check.append([i, j])
                else:
                    heats.append([i, j, temp[j]])
                temp[j] = 0
        board.append(temp)

    new = [[0] * (M*2) for _ in range(N*2)]

    W = int(input())

    for _ in range(W):
        x, y, c = map(int, input().split())
        nx = (x-1) * 2
        ny = (y-1) * 2
        if c == 1:
            new[nx][ny+1] = 1
        else:
            new[nx-1][ny] = 1



    T = 0
    while T < 101:

        #heat on


        for x, y, c in heats:
            temp_board = [[0] * M for _ in range(N)]
            visited = [[0] * M for _ in range(N)]
            nx, ny = x + kx[c], y + ky[c]
            dfs(nx, ny, c, 5, N, M)



        #chocolate
        T += 1

        #온도 조절
        visited = [[0] * M for _ in range(N)]
        tmp_board = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                temp_avg(i, j)

        for i in range(N):
            for j in range(M):
                new[i*2][j*2] += tmp_board[i][j]



        for i in range(M):
            if new[0][i*2] > 0:
                new[0][i*2] -= 1
            if new[-2][i*2] > 0:
                new[-2][i*2] -= 1

        for i in range(1, N-1):
            if new[i*2][0] > 0:
                new[i*2][0] -= 1

            if new[i*2][-2] > 0:
                new[i*2][-2] -= 1




        #바깥 온도 -1

        cnt = 0
        all = len(check)
        for i, j in check:
            if new[i*2][j*2] >= K:
                cnt += 1

        if cnt == all:
            break

    print("#%d %d" % (test_case+1, T))


"""
9
7 8 1
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 5
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 7
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 70
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 1000
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 100
0 0 0 0 0 0 0 0
5 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
5 0 0 0 0 0 5 0
0 0 0 0 3 0 0 0
0
7 8 100
0 0 0 0 0 0 5 0
5 4 4 4 4 4 4 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
5 0 0 0 0 0 5 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 1000
0 0 0 0 0 0 5 0
5 4 4 4 4 4 4 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
5 0 0 0 0 0 5 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
7 8 1000
0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4
0 0 0 0 0 5 0 0
0 0 5 5 0 0 5 0
0 0 0 0 0 5 0 0
5 0 0 0 0 0 5 0
3 3 3 3 3 3 3 3
3
4 4 1
5 4 0
5 6 0
"""