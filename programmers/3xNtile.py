def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1

    sum_ = 0
    for i in range(2, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum_ * 2
        sum_ += dp[i - 2]

    answer = dp[n] % 1000000007

    """
    2칸을 쓸 때 경우의 수 3
    4칸을 쓸 때 경우의 수 2
    6칸을 쓸 때 경우의 수 2
    8칸을 쓸 때 경우의 수 2
    .
    .
    .
    단순하게 2칸만 생각 해서 문제가 풀리지 않았는데
    몇 칸을 차지할 때의 경우의 수를 잘 파악해야 한다.
    펜이나 종이는 필수
    """

    return answer