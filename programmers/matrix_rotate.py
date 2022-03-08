dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def init(row, col):
    mat = [[i * col + j + 1 for j in range(col)] for i in range(row)]
    return mat

def roll(mat, query):
    x, y, nx, ny = query
    x -= 1
    y -= 1
    nx -= 1
    ny -= 1

    min_ = int(1e9)
    prev = mat[x][y]

    #상단


    for i in range(y, ny):
        min_ = min(prev, min_)
        nxt = mat[x][i+1]
        mat[x][i+1] = prev
        prev = nxt

    for i in range(x, nx):
        min_ = min(prev, min_)
        nxt = mat[i+1][ny]
        mat[i+1][ny] = prev
        prev = nxt

    for i in range(ny, y, -1):
        min_ = min(prev, min_)
        nxt = mat[nx][i-1]
        mat[nx][i-1] = prev
        prev = nxt

    for i in range(nx, x, -1):
        min_ = min(prev, min_)
        nxt = mat[i-1][y]
        mat[i-1][y] = prev
        prev = nxt

    min_ = min(prev, min_)
    return min_


def solution(rows, columns, queries):
    mat = init(rows, columns)
    answer = []
    for query in queries:
        answer.append(roll(mat, query))
    return answer




rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

print(solution(rows, columns, queries))