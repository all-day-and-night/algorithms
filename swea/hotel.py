"""
백준 1106 호텔
"""

C, N = map(int, input().split())

cities = []

for _ in range(N):
    cost, customers = map(int, input().split())
    cities.append([cost, customers])

cities.sort(key=lambda x:(x[0]))



INF = 100 * 1000
dp = [INF] * (C+100)
dp[0] = 0
res = INF

for cost, client in cities:
    for i in range(client, C+100):
        dp[i] = min(dp[i-client] + cost, dp[i])
        if i >= C:
            res = min(dp[i], res)

print(res)



