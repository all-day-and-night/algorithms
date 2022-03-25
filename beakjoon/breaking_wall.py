from heapq import heappush, heappop

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(input()))



q = []

INF = int(1e9)
distance = [[[INF] * 2 for _ in range(M)] for _ in range(N)]

distance[0][0][0] = 1

heappush(q, [1, 0, 0, 0])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


while q:
    dist, x, y, is_break = heappop(q)

    if x == N-1 and y == M-1:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue

        if is_break == 0 and board[nx][ny] == '1':
            if distance[nx][ny][1] > dist + 1:
                distance[nx][ny][1] = dist + 1
                heappush(q, [dist + 1, nx, ny, 1])
                continue

        if board[nx][ny] == '0':
            if distance[nx][ny][is_break] > dist + 1:
                distance[nx][ny][is_break] = dist + 1
                heappush(q, [dist + 1, nx, ny, is_break])

answer = min(distance[N-1][M-1])
if answer == INF:
    print(-1)
else:
    print(answer)