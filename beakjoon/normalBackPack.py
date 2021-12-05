N, K = map(int, input().split())

data = [[0, 0]]

for _ in range(N):
    data.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = data[i]
    for j in range(1, K+1):
        # 담을 물건의 크기가 배낭의 크기보다 작을 경우 위의 값을 그대로 가져온다.
        if j < w:
            dp[i][j] = dp[i-1][j]
        #그렇지 않을 경우 현재 물건을 담고 현재 물건의 무게를 제외한 이전의 최적값을 더하고
        #현재 물건을 담지 않은 최적값과 비교하여 dp 할당
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])
