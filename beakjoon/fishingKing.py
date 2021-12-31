"""
1. 낚시왕 이동(가장 끝에 도달하면 끝)
2. 가까운 상어 잡기
3. 상어 이동 (같은 공간에 있을 경우 큰 상어가 남음

분명히 쉬운 문제인데 연습을 너무 안한듯

물고기를 바로 이동할 수 있는 식 세우기
"""

from copy import deepcopy


def fishing(maps, R, idx):
    result = 0
    for i in range(R):
        if maps[i][idx] != 0:
            result = maps[i][idx][2]
            maps[i][idx] = 0
            break
    return result

R, C, M = map(int, input().split())

maps = [[0] * C for _ in range(R)]

for i in range(M):
    x, y, s, d, z = map(int, input().split())
    maps[x-1][y-1] = [s, d, z]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
for k in range(C):
    result += fishing(maps, R, k)
    new_maps = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if maps[i][j] != 0:
                s, d, z = maps[i][j]
                x, y = i, j
                cnt = 0

                while cnt < s:
                    nx, ny = x + dx[d-1], y + dy[d-1]
                    if nx < 0 or ny < 0 or nx > R-1 or ny > C-1:
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3
                        continue

                    cnt += 1
                    x, y = nx, ny

                if new_maps[x][y] == 0:
                    new_maps[x][y] = [s, d, z]
                else:
                    if new_maps[x][y][2] < z:
                        new_maps[x][y] = [s, d, z]

    maps = deepcopy(new_maps)
print(result)






