from collections import deque


def solution(order):
    answer = 0
    stack = []
    q = [0] * len(order)
    for i, o in enumerate(order):
        q[o - 1] = i + 1
    q = deque(q)
    idx = 1

    while q:

        if q[0] == idx:
            q.popleft()
            answer += 1
            idx += 1

        else:
            if stack and stack[-1] == idx:
                stack.pop()
                idx += 1
                answer += 1
            else:
                stack.append(q.popleft())

    while stack:
        if stack[-1] == idx:
            answer += 1
            idx += 1
            stack.pop()
        else:
            break

    return answer