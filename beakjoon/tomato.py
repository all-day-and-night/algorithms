from collections import deque

M, N = map(int, input().split())

board = []
tomato = deque()
cnt = 0
cannot =- 0
for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(M):
        if temp[j] == 1:
            tomato.append([i, j, 0])
            cnt += 1
        elif temp[j] == -1:
           cannot += 1
    board.append(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

if cnt == N * M - cannot:
    print(0)

else:
    answer = 0
    while tomato:
        x, y, day = tomato.popleft()
        answer = max(answer, day)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if board[nx][ny] == 0:
                tomato.append([nx, ny, day+1])
                board[nx][ny] = 1
                cnt += 1

    if cnt == N*M - cannot:
        print(answer)
    else:
        print(-1)


