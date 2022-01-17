import copy


def calc(info, lion):
    result = 0
    for i in range(len(info) - 1):
        if info[i] > lion[i]:
            result -= (10 - i)
        elif info[i] < lion[i]:
            result += (10 - i)
        elif info[i] == lion[i]:
            if info[i] != 0:
                result -= (10 - i)

    return result


array = []


def dfs(cnt, idx, visited, info, n):
    if cnt > n:
        return
    if cnt == n:
        store = copy.deepcopy(visited)
        array.append(store)
        return
    if idx > 10:
        visited[10] += (n - cnt)
        store = copy.deepcopy(visited)
        visited[10] -= (n - cnt)
        array.append(store)
        return

    # 맞춤
    if info[idx] > 0:
        visited[idx] = info[idx] + 1
        dfs(cnt + visited[idx], idx + 1, visited, info, n)
        visited[idx] = 0
    elif info[idx] == 0:
        visited[idx] = 1
        dfs(cnt + 1, idx + 1, visited, info, n)
        visited[idx] = 0

    # 안맞춤
    dfs(cnt, idx + 1, visited, info, n)
    return


def compare(a, b):
    for i in range(10, -1, -1):
        if a[i] > b[i]:
            return 0
        elif a[i] < b[i]:
            return 1


def solution(n, info):
    answer = []
    visited = [0 for _ in range(11)]
    dfs(0, 0, visited, info, n)

    max_ = 0
    for a in array:
        temp = calc(info, a)
        if max_ < temp:
            max_ = temp
            answer = a
        elif max_ == temp and len(answer) > 0:
            if compare(answer, a) == 1:
                answer = a

    if max_ == 0:
        return [-1]

    return answer