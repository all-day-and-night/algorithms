def dfs(arr):
    # 4개로 분할
    len_ = len(arr)
    if len_ == 1:
        if arr[0][0] == 0:
            return [1, 0]
        else:
            return [0, 1]

    value = arr[0][0]
    compact = True
    for i in range(len_):
        for j in range(len_):
            if arr[i][j] != value:
                compact = False
        if not compact:
            break

    if compact:
        if value == 0:
            return [1, 0]
        else:
            return [0, 1]

    arr1 = [[0] * (len_ // 2) for _ in range(len_ // 2)]
    arr2 = [[0] * (len_ // 2) for _ in range(len_ // 2)]
    arr3 = [[0] * (len_ // 2) for _ in range(len_ // 2)]
    arr4 = [[0] * (len_ // 2) for _ in range(len_ // 2)]

    for i in range(len_ // 2):
        for j in range(len_ // 2):
            arr1[i][j] = arr[i][j]

    for i in range(len_ // 2):
        for j in range(len_ // 2):
            arr2[i][j] = arr[i][j + len_ // 2]

    for i in range(len_ // 2):
        for j in range(len_ // 2):
            arr3[i][j] = arr[i + len_ // 2][j]

    for i in range(len_ // 2):
        for j in range(len_ // 2):
            arr4[i][j] = arr[i + len_ // 2][j + len_ // 2]
    result = [0, 0]
    a1 = dfs(arr1)
    a2 = dfs(arr2)
    a3 = dfs(arr3)
    a4 = dfs(arr4)
    result[0] = result[0] + a1[0] + a2[0] + a3[0] + a4[0]
    result[1] = result[1] + a1[1] + a2[1] + a3[1] + a4[1]

    return result


def solution(arr):
    answer = []
    answer = dfs(arr)

    return answer