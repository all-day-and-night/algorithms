dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find(key, value, board, N):
    x, y = 0, 0
    likes = -1
    blanks = -1
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            like = 0
            blank = 0
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                    continue
                if board[ni][nj] == 0:
                    blank += 1
                if board[ni][nj] in value:
                    like += 1
            if likes < like:
                likes = like
                blanks = blank
                x, y = i, j
            elif likes == like and blanks < blank:
                blanks = blank
                x, y = i, j
    board[x][y] = key
    return x, y

def getSatisfaction(board, N, data):
    result = 0
    num = [0, 1, 10, 100, 1000]
    for x in range(N):
        for y in range(N):
            key = board[x][y]
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    continue
                if board[nx][ny] in data[key]:
                    cnt += 1
            result += num[cnt]
    return result

N = int(input())

data = {}
for _ in range(N*N):
    d = list(map(int, input().split()))
    data[d[0]] = set(d[1:])

board = [[0] * N for _ in range(N)]


for key, value in data.items():
    find(key, value, board, N)

answer = getSatisfaction(board, N, data)
print(answer)