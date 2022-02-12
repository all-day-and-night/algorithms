def solution(board, moves):
    answer = 0
    row = len(board)
    col = len(board[0])

    new = [[] for _ in range(col)]

    for i in range(row - 1, -1, -1):
        for j in range(col):
            if board[i][j] != 0:
                new[j].append(board[i][j])

    stack = []

    for move in moves:
        if new[move - 1]:
            now = new[move - 1].pop()
            if stack and stack[-1] == now:
                stack.pop()
                answer += 2
            else:
                stack.append(now)

    return answer