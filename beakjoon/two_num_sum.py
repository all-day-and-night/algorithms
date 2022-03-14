N = int(input())

data = list(map(int, input().split()))

X = int(input())

data.sort()

left = 0
right = len(data)-1

answer = 0
while left < right:
    value = data[left] + data[right]

    if value == X:
        answer += 1
        left += 1
        right -= 1

    elif value > X:
        right -= 1

    elif value < X:
        left += 1

print(answer)
