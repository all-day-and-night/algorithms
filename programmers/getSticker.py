def sol(stick, dp, value):
    result = value
    dp[0] = stick[0]
    dp[1] = max(stick[0], stick[1])
    for i in range(2, len(stick)):
        dp[i] = max(dp[i - 2] + stick[i], dp[i - 1], dp[i - 3] + stick[i])

    result += dp[-1]
    return result


def solution(sticker):
    answer = 0

    if len(sticker) < 4:
        return max(sticker)

    sticker = sticker
    # 1번을 골랐을 때
    stick1 = sticker[2:-1]
    dp1 = [0] * len(stick1)
    # 마지막을 골랐을 때
    stick2 = sticker[1:-2]
    dp2 = [0] * len(stick2)
    # 둘 다 안 골랐을 때
    stick3 = sticker[1:-1]
    dp3 = [0] * len(stick3)

    result1 = sol(stick1, dp1, sticker[0])
    result2 = sol(stick2, dp2, sticker[-1])
    result3 = sol(stick3, dp3, 0)

    answer = max(result1, result2, result3)

    return answer