from collections import deque
import itertools

N, K = map(int, input().split())

data = list(map(int, input().split()))

data = deque(data)
stack = []
answer = 0
while data:
    if len(stack) < N:
        if data[0] not in stack:
            stack.append(data.popleft())
        else:
            data.popleft()

    if len(stack) == N and data:
        if data[0] in stack:
            data.popleft()
            continue

        a = 0
        b = 0
        for i in range(len(stack)):
            if stack[i] not in data:
                b = i
                break
            else:
                if a < data.index(stack[i]):
                    a = data.index(stack[i])
                    b = i
        stack.pop(b)
        answer += 1

print(answer)


