import sys

input = sys.stdin.readline

N = int(input())

#0은 아무것도 안고름, 1은 왼쪽만 고름, 2는 오른쪽만 고름

dp = [[0] * 3 for _ in range(N)]

dp[0][0], dp[0][1], dp[0][2] = 1, 1, 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[N-1]) % 9901)