def solution(N, stages):
    answer = []

    check = [0] * (N + 2)

    for stage in stages:
        check[stage] += 1

    users = [0] * (N + 2)
    users[-1] = check[-1]
    for i in range(len(check) - 1, 1, -1):
        users[i - 1] = users[i] + check[i - 1]

    fail = []
    for i in range(1, N + 1):
        if users[i] == 0:
            fail.append([0, i])
        else:
            fail.append([(-1) * check[i] / users[i], i])
    fail.sort(key=lambda x: (x[0], x[1]))

    for a, b in fail:
        answer.append(b)
    return answer