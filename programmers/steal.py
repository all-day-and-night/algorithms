def sol(money, dp):
    dp = [0] * (len(money))
    dp[0] = money[0]
    if money[0] > money[1]:
        dp[1] = money[0]
    else:
        dp[1] = money[1]
    for i in range(2, len(money)):
        if money[i] + dp[i-2] > dp[i-1]:
            dp[i] = money[i] + dp[i-2]
        else:
            dp[i] = dp[i-1]
    return dp[len(money)-1]

def solution(money):
    answer = max(sol(money[:-1], [0] * (len(money)-1) ), sol(money[1:], [0] * (len(money)-1) ))
    return answer