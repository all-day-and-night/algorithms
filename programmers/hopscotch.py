def solution(land):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    row = len(land)
    col = len(land[0])
    dp = [[0] * col for _ in range(row)]
    for i in range(col):
        dp[0][i] = land[0][i]

    for i in range(1, row):
        for j in range(col):
            temp = dp[i - 1][0:j] + dp[i - 1][j + 1:]
            dp[i][j] = max(temp) + land[i][j]

    return max(dp[row - 1])