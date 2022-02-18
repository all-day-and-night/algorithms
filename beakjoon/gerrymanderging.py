"""
단순 구현문제인데 한시간 반정도 썼다.
헷갈릴 때는 그냥 padding 넣어서 값 일치 시키는게 가장 좋을 듯
해보자!
"""

def sol(board, x, y, d1, d2, N, total):
    cnts = [0] * 5
    check = [[0] * (N+1) for _ in range(N+1)]

    check[x][y] = 5
    for i in range(1, d1 + 1):
        check[x+i][y-i] = 5

    for i in range(1, d2 + 1):
        check[x + i][y + i] = 5

    for i in range(1, d2+1):
        check[x + d1 + i][y - d1 + i] = 5

    for i in range(1, d1+1):
        check[x + d2 + i][y + d2 - i] = 5

    #1번
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if check[i][j] == 5:
                break
            else:
                cnts[0] += board[i][j]
    #2
    for i in range(1, x + d2 + 1):
        for j in range(N, y, -1):
            if check[i][j] == 5:
                break
            else:
                cnts[1] += board[i][j]
    #3
    for i in range(x+d1, N+1):
        for j in range(1, y - d1 + d2):
            if check[i][j] == 5:
                break
            else:
                cnts[2] += board[i][j]
    #4
    for i in range(x + d2+1, N+1):
        for j in range(N, y - d1 + d2 - 1, -1):
            if check[i][j] == 5:
                break
            else:
                cnts[3] += board[i][j]

    cnts[4] = total - sum(cnts)
    return max(cnts) - min(cnts)

N = int(input())

board = []
board.append([0] * (N+1))

total = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    total += sum(temp)
    temp = [0] + temp
    board.append(temp)

answer = int(1e9)

for x in range(1, N):
    for y in range(1, N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if y - d1 < 1:
                    continue

                if y + d2 > N :
                    continue

                if x + d1 + d2 > N:
                    continue

                answer = min(answer, sol(board, x, y, d1, d2, N, total))
print(answer)