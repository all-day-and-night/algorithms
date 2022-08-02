from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def solution(N, sx, sy, ex, ey):
    INF = int(1e9)
    board = [[INF] * N for _ in range(N)]
    board[sx][sy] = 0


    q = deque()
    q.append([sx, sy, 0])
    x, y = sx, sy
    while q:
        x, y, cost = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if board[nx][ny] > cost + 1:
                board[nx][ny] = cost + 1
                q.append([nx, ny, cost + 1])

    print(board[ex][ey])






T = int(input())

for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    solution(N, sx, sy, ex, ey)