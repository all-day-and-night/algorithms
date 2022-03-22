N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, list(input()))))

dp = [[0] * (M+1) for _ in range(N+1)]

answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            answer = max(answer, dp[i][j])


print(answer ** 2)

