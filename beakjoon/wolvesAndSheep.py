N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
isTrue = True
for i in range(N):
    for j in range(M):

        if board[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 'S':
                    isTrue = False
                    break

        elif board[i][j] == 'S':
            continue

        elif board[i][j] == '.':
            board[i][j] = 'D'

if isTrue:
    print(1)
    for b in board:
        print(''.join(b))
else:
    print(0)
