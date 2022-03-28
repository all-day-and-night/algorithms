N = int(input())

data = list(map(int, input().split()))
data = [0] + data
INF = int(1e9)
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))