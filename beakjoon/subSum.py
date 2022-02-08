N, S = map(int, input().split())

data = list(map(int, input().split()))

left = 0
right = 0

answer = len(data) + 1
sum_ = 0
while left < N:
    if sum_ >= S:
        answer = min(answer, right - left)
        sum_ -= data[left]
        left += 1

    else:
        if right > N-1:
            break
        else:
            sum_ += data[right]
            right += 1


if answer == len(data) + 1:
    print(0)
else:
    print(answer)