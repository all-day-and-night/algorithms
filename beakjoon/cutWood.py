N, M = map(int, input().split())

woods = list(map(int, input().split()))

left = 0
right = max(woods)

while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for wood in woods:
        if wood > mid:
            cnt += wood - mid

    if cnt >= M:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)