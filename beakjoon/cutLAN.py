K, N = map(int, input().split())

lans = []
for _ in range(K):
    lans.append(int(input()))

left = 0
right = max(lans)
answer = 0


while left <= right:
    mid = (left + right) // 2
    if mid == 0:
        answer = 1
        break

    cnt = 0
    for lan in lans:
        cnt += lan // mid

    if cnt >= N:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)