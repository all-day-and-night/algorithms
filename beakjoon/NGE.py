N = int(input())

data = list(map(int, input().split()))

answer = [0] * N

stack = []

for i in range(N-1, -1, -1):
    print(i, stack)
    while stack and stack[-1] <= data[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1]
    else:
        answer[i] = -1
    stack.append(data[i])
print(answer)
