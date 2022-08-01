N, M = map(int, input().split())

data = list(map(int, input().split()))

left = max(data)
right = sum(data)

answer = int(1e9)
while left <= right:
    mid = (left + right) // 2

    cnt = 1
    sums = 0
    for i in range(N):
        if sums + data[i] <= mid:
            sums += data[i]
        else:
            cnt += 1
            sums = data[i]

    if cnt <= M:
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)


