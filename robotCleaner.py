"""

비슷한 문제를 풀어본 경험이 있어서 문제를 대충 읽었음
때문에 세세한 부분에서 오류가 생겨서 금방 풀지 못함

"""


"""import sys

input = sys.stdin.readline


N, M = map(int, input().split())
r, c, dir_ = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = r, c
cnt = 1
data[x][y] = 2
while True:
    ischeck = True
    for _ in range(4):
        dir_ = (dir_ + 3) % 4
        nx, ny = x + dx[dir_], y + dy[dir_]
        if 0 <= nx < N and 0 <= ny < M:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                cnt += 1
                x, y = nx, ny
                ischeck = False
                break

    if ischeck:
        nx, ny = x - dx[dir_], y - dy[dir_]
        if 0 <= nx < N and 0 <= ny < M:
            if data[nx][ny] == 2:
                x, y = nx, ny
            elif data[nx][ny] == 1:
                break
        else:
            break

print(cnt)
"""


"""
이번에는 재귀함수로 문제를 풀어볼거임
"""



