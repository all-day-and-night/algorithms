N = int(input())

def dfs(x, y, len_):
    if len_ == 1:
        if board[x][y] == 1:
            return [1, 0]
        else:
            return [0, 1]
    key = board[x][y]

    for i in range(x, x + len_):
        for j in range(y, y + len_):
            if board[i][j] != key:
                result = [0, 0]
                a, b = dfs(x, y, len_ // 2)
                result[0] += a
                result[1] += b
                a, b = dfs(x, y + len_ // 2, len_ // 2)
                result[0] += a
                result[1] += b

                a, b = dfs(x + len_ // 2, y, len_ // 2)
                result[0] += a
                result[1] += b

                a, b = dfs(x + len_ // 2, y + len_ // 2, len_ // 2)
                result[0] += a
                result[1] += b

                return result

    if key == 1:
        return [1, 0]
    else:
        return [0, 1]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = dfs(0, 0, N)
print(answer[1])
print(answer[0])