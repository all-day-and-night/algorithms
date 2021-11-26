from collections import deque


def bfs(board, direction):
    N = len(board)
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    # i, j, cost, dir
    q.append([0, 0, 0, direction])
    distance[0][0] = 0
    while q:
        x, y, cost, dir_ = q.popleft()

        if x == N - 1 and y == N - 1:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # out of range
            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                continue
            # wall
            if board[nx][ny] == 1:
                continue
            ncost = 0
            if dir_ == i or dir_ == -1:
                ncost = cost + 100
            else:
                ncost = cost + 600

            if distance[nx][ny] >= ncost:
                distance[nx][ny] = ncost
                q.append([nx, ny, ncost, i])

    return distance[-1][-1]


def solution(board):
    answer = 0

    return min(bfs(board, 0), bfs(board, 1))