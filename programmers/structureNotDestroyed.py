def solution(board, skill):
    answer = 0
    new_board = [[0] * len(board[0]) for _ in range(len(board))]

    for types, x1, y1, x2, y2, value in skill:
        # 부수기
        much = 0
        if types == 1:
            much = value * (-1)
        # 회복
        else:
            much = value

        row = abs(x1 - x2) + 1
        col = abs(y1 - y2) + 1
        x = min(x1, x2)
        y = min(y1, y2)
        new_board[x][y] += much
        if y + col < len(board[0]):
            new_board[x][y + col] -= much

        if x + row < len(board):
            new_board[x + row][y] -= much

        if y + col < len(board[0]) and x + row < len(board):
            new_board[x + row][y + col] += much

    for i in range(1, len(new_board)):
        for j in range(len(new_board[0])):
            new_board[i][j] += new_board[i - 1][j]

    for j in range(1, len(new_board[0])):
        for i in range(len(new_board)):
            new_board[i][j] += new_board[i][j - 1]

    cnt = 0

    for i in range(0, len(new_board)):
        for j in range(0, len(new_board[0])):
            board[i][j] += new_board[i][j]
            if board[i][j] > 0:
                cnt += 1
    return cnt