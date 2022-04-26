N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))


x, y = N // 2, N // 2



dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 0

cnt = 0
step = 1

maps = [
    [[0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]]
]

def rotate(m):
    new = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            new[4 - j][i] = m[i][j]

    return new
m1 = rotate(maps[0])
m2 = rotate(m1)
m3 = rotate(m2)

maps.append(m1)
maps.append(m2)
maps.append(m3)

answer = 0

while step < N+1:
    for i in range(step):
        nx, ny = x + dx[d], y + dy[d]

        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            step += 1
            continue
        #로직 넣으면 돼

        #모래 이동
        """
        board[nx][ny] += board[x][y]
        board[x][y] = 0
        """

        #흘날리기

        x, y = nx, ny

        sands = board[x][y]

        outs = 0
        alpha = 0
        all = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x + i, y + j
                now = int(sands * maps[d][i+2][j+2] / 100)
                if now == 0:
                    continue

                #outs
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    outs += now
                    all += now
                    continue

                # in
                board[nx][ny] += now
                all += now

        alpha = sands - all
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
            outs += alpha

        else:
            board[nx][ny] += alpha

        answer += outs

    if d == 1 or d == 3:
        step += 1
    d = (d + 1) % 4


print(answer)