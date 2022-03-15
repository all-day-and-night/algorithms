N = int(input())

def dfs(x, y, len_):
    if len_ == 1:
        if board[x][y] == '1':
            return "1"
        else:
            return "0"
    key = board[x][y]

    for i in range(x, x + len_):
        for j in range(y, y + len_):
            if board[i][j] != key:

                a = dfs(x, y, len_ // 2)
                b = dfs(x, y + len_ // 2, len_ // 2)
                c = dfs(x + len_ // 2, y, len_ // 2)
                d = dfs(x + len_ // 2, y + len_ // 2, len_ // 2)

                return "(" + a + b + c + d + ")"

    if key == '1':
        return "1"
    else:
        return "0"

board = []
for _ in range(N):
    board.append(list(input()))

answer = dfs(0, 0, N)
print(answer)