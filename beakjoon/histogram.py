def sol(data):
    stack = []
    answer = 0

    for d in data:
        width = 0
        while stack and stack[-1][0] > d:
            width += stack[-1][1]
            answer = max(answer, stack.pop()[0] * width)

        width += 1
        stack.append([d, width])

    width = 0
    while stack:
        width += stack[-1][1]
        answer = max(answer, stack.pop()[0] * width)

    return answer


if __name__ == '__main__':
    answer = []
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0:
            break

        answer.append(sol(data[1:]))

    for ans in answer:
        print(ans)
