def solution(N, coins, value):
    dp = [0] * (value + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(value + 1):
            if i >= coin:
                dp[i] += dp[i-coin]
    return dp[value]


T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    value = int(input())

    print(solution(N, coins, value))
