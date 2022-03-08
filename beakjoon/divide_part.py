"""
최소값 중 최대값을 구하라는 등의 문제는

parametric search을 사용해야 하는 것이 좋을 듯
"""

N, M = map(int, input().split())

data = list(map(int, input().split()))

start, end = 0, max(data)
answer = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    min_, max_ = data[0], data[0]

    for i in range(1, N):
        min_ = min(min_, data[i])
        max_ = max(max_, data[i])

        if max_ - min_ > mid:
            cnt += 1
            min_ = data[i]
            max_ = data[i]

    if cnt <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)