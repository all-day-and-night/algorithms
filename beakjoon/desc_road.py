import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

distance = [[-1] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1

    if distance[x][y] != -1:
        return distance[x][y]

    distance[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue
        if board[x][y] > board[nx][ny]:
            distance[x][y] += dfs(nx, ny)

    return distance[x][y]

print(dfs(0, 0))