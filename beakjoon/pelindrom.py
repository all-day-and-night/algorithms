import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for len_ in range(1, N):
    for start in range(N - len_):
        end = start + len_

        if data[start] == data[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

M = int(input())

args = []
for _ in range(M):
    a, b = map(int, input().split())
    args.append([a, b])

for a, b in args:
    print(dp[a-1][b-1])