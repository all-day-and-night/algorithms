"""N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 부분의 개수 입력
K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

"""
N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))


sums = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        sums[i+1][j+1] = sums[i][j+1] + sums[i+1][j] + board[i][j] - sums[i][j]




T = int(input())

for _ in range(T):
    x, y, nx, ny = map(int, input().split())

    print(sums[nx][ny] + sums[x-1][y-1] - sums[x-1][ny] - sums[nx][y-1])