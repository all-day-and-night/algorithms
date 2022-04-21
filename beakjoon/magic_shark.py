import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(N):
    board.append(list(map(int, input().split())))



inputs = []
for _ in range(M):
    inputs.append(list(map(int, input().split())))


def move_cloud(di, si):
    for i in range(len(cloud)):
        x, y = cloud[i]
        nx, ny = (x + si * dx[di]) % N, (y + si * dy[di]) % N
        cloud[i] = [nx, ny]


def get_rain():
    for i in range(len(cloud)):
        x, y = cloud[i]
        board[x][y] += 1


def get_cloud(prev):
    result = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1 and prev[i][j] == 0:
                result.append([i, j])
                board[i][j] -= 2

    return result


def get_water():
    for i in range(len(cloud)):
        cnt = 0
        for ddx, ddy in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
            nx, ny = (cloud[i][0] + ddx), (cloud[i][1] + ddy)
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if board[nx][ny] > 0:
                cnt += 1

        board[cloud[i][0]][cloud[i][1]] += cnt


prev = [[0] * N for _ in range(N)]

move_cloud(inputs[0][0]-1, inputs[0][1])
get_rain()
get_water()
for x, y in cloud:
    prev[x][y] = 1

cloud = get_cloud(prev)



for inp in inputs[1:]:
    di, si = inp
    move_cloud(inp[0] - 1, inp[1])

    get_rain()

    get_water()

    prev = [[0] * N for _ in range(N)]
    for x, y in cloud:
        prev[x][y] = 1
    cloud = get_cloud(prev)

ans = 0
for c in board:
    ans += sum(c)

print(ans)
