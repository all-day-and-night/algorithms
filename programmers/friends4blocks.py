"""def down(block, n, m):
    for i in range(n):
        temp = [item for item in block[i] if item != '0']
        temp.extend([0] *(m - len(temp)))
        block[i] = temp

def check(block, i, j):

    if block[i][j] == block[i+1][j+1] == block[i][j+1] == block[i+1][j]:
        return True
    return False

def erase(block, i, j):
    cnt = 0
    for k in range(i, i+2):
        for l in range(j, j+2):
            if block[k][l] == '0':
                continue
            else:
                block[k][l] = '0'
                cnt += 1
    return cnt

def sol(block, n, m):
    cnt = 0
    remove = []
    for i in range(n-1):
        for j in range(m-1):
            if block[i][j] == 0:
                continue
            if check(block, i, j):
                remove.append([i, j])
    for r in remove:
        cnt += erase(block, r[0], r[1])
    down(block, n, m)
    return cnt

def solution(m, n, board):
    answer = 0
    new = [[0] * m for _ in range(n)]
    #rotate <- 이쪽으로
    for i in range(n):
        for j in range(m):
            new[n-1-i][m-j-1] = board[j][n-i-1]


    while True:
        temp = sol(new, n, m)
        if temp == 0:
            break
        else:
            answer += temp

    return answer

"""


def check(x, y, board):
    key = board[x][y]
    for nx, ny in [[x + 1, y], [x, y + 1], [x + 1, y + 1]]:
        if board[nx][ny] != key:
            return False
    return True


def sol(n, m, board):
    remove = []
    for i in range(n - 1):
        for j in range(m - 1):
            if check(i, j, board):
                remove.append([i, j])

    if len(remove) == 0:
        return 0
    cnt = 0
    for x, y in remove:
        for nx, ny in [[x, y], [x + 1, y], [x, y + 1], [x + 1, y + 1]]:
            if board[nx][ny] != 0:
                cnt += 1
                board[nx][ny] = 0

    for i in range(n):
        temp = [j for j in board[i] if j != 0]
        temp += [0] * (n - len(temp))
        board[i] = temp

    return cnt


def solution(m, n, board):
    new_board = [[0] * m for _ in range(n)]

    # rotate <- 방향
    """
    M-1, 0 -> 0, 0
    0, 0 -> 0, N-1
    """
    for i in range(m):
        for j in range(n):
            new_board[j][m - 1 - i] = board[i][j]

    answer = 0
    while True:
        cnt = sol(n, m, new_board)
        if cnt == 0:
            break
        answer += cnt
    return answer


