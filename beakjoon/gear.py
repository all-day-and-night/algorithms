def clockwise(d):
    return (d-1) % 8

def counterclockwise(d):
    return (d+1) % 8

def gearRotation(gidx, gnum, dir_, check):
    for i in range(4):
        if check[i] == 0:
            continue
        ndir = -1
        if (gnum-i) % 2 == 0:
            ndir = dir_
        else:
            ndir = (-1) * dir_

        if ndir == 1:
            gidx[i] = clockwise(gidx[i])
        else:
            gidx[i] = counterclockwise(gidx[i])



gears = []

for _ in range(4):
    gears.append(list(input()))


gidx = [2, 2, 2, 2]

N = int(input())

for _ in range(N):
    gnum, dir_ = map(int, input().split())
    check = [0] * 4
    check[gnum-1] = 1

    for i in range(gnum-1, 4):
        if i+1 > 3:
            break
        if gears[i][gidx[i]] != gears[i+1][(gidx[i+1] + 4) % 8]:
            check[i+1] = 1
        else:
            break

    for i in range(gnum-1, -1, -1):
        if i-1 < 0:
            break
        if gears[i][(gidx[i] + 4) % 8] != gears[i - 1][gidx[i-1]]:
            check[i - 1] = 1
        else:
            break

    gearRotation(gidx, gnum-1, dir_, check)


score = 0


if gears[0][(gidx[0] - 2) % 8] == '1':
    score += 1

if gears[1][(gidx[1] - 2) % 8] == '1':
    score += 2

if gears[2][(gidx[2] - 2) % 8] == '1':
    score += 4

if gears[3][(gidx[3] - 2) % 8] == '1':
    score += 8

print(score)
