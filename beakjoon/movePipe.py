"""
시간복잡도를 고려해서 문제를 풀어야 한다.

그래프 문제일 것이라고 생각해서 bfs로 풀었지만

시간제한에 걸렸다

dp로 시간을 줄여 풀었는데

수평, 수직, 대각선의 경우에 따라 dp 맵을 구현해서

O(N * N) (3<= N <= 16) 최대 16 ^ 2 으로 시간을 줄였다.
"""

from collections import deque

N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# 수평
dp1 = [[0] * N for _ in range(N)]
dp1[0][1] = 1
# 수직
dp2 = [[0] * N for _ in range(N)]
# 대각선
dp3 = [[0] * N for _ in range(N)]

for i in range(2, N):
    if board[0][i] == 0:
        dp1[0][i] += dp1[0][i-1]
    else:
        break

for i in range(1, N):
    for j in range(1, N):
        if board[i][j] + board[i-1][j] + board[i][j-1] == 0:
            dp3[i][j] += dp3[i-1][j-1]
            dp3[i][j] += dp2[i-1][j-1]
            dp3[i][j] += dp1[i-1][j-1]
        if board[i][j] == 0:
            dp2[i][j] += dp3[i-1][j]
            dp2[i][j] += dp2[i-1][j]

            dp1[i][j] += dp1[i][j-1]
            dp1[i][j] += dp3[i][j-1]



answer = dp1[N-1][N-1] + dp2[N-1][N-1] + dp3[N-1][N-1]
print(answer)
"""q.append([0, 1, 0])

while q:
    x, y, dir_ = q.popleft()

    move = []
    if dir_ == 0:
        move.append(0)
        move.append(2)
    elif dir_ == 1:
        move.append(1)
        move.append(2)
    elif dir_ == 2:
        move.append(0)
        move.append(1)
        move.append(2)

    for m in move:
        nx, ny = x + dx[m], y + dy[m]
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            continue

        if m == 2:
            if board[nx-1][ny] == 1 or board[nx][ny-1] == 1:
                continue

        if board[nx][ny] == 0:
            q.append([nx, ny, m])
            distance[nx][ny] += 1

print(distance[N-1][N-1])"""


