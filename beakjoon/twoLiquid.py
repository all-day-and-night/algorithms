N = int(input())

data = list(map(int, input().split()))

data.sort()

left = 0
right = len(data)-1

prev = int(1e10)
answer = [0, 0]
while left < right:
    now = abs(data[left] + data[right])

    if now < prev:
        answer = data[left], data[right]
        prev = now

    if abs(data[left+1] + data[right]) > abs(data[left] + data[right-1]):
        right -= 1
    else:
        left += 1

print(answer[0], answer[1])

