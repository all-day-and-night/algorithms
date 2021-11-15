import sys

def check(row, N, L):
    prev = row[0]
    incline = [0] * N
    for i in range(N):
        if prev == row[i]:
            continue

        #now != row[i]
        else:
            if abs(prev-row[i]) > 1:
                return False

            #desc
            if prev > row[i]:
                if i+L <= N:
                    for j in range(L):
                        if i + j > N-1:
                            return False
                        if row[i+j] != row[i]:
                            return False

                    for j in range(L):
                        if i + j > N-1:
                            return False
                        if incline[i+j] == 1:
                            return False

                    for j in range(L):
                        if i + j > N-1:
                            return False
                        incline[i+j] = 1
                    prev = row[i]
                    continue

                else:
                    return False

            #asc
            if prev < row[i]:
                if i >= L:
                    for j in range(L):
                        if i - j - 1 < 0:
                            return False
                        if row[i-j-1] != prev:
                            return False
                    for j in range(L):
                        if i - j - 1 < 0:
                            return False
                        if incline[i-j-1] == 1:
                            return False

                    for j in range(L):
                        if i - j - 1 < 0:
                            return False
                        incline[i-j-1] = 1
                    prev = row[i]
                    continue
                else:
                    return False
    return True








input = sys.stdin.readline

N, L = map(int, input().split())

map_ = []
cnt = 0
for _ in range(N):
    map_.append(list(map(int, input().split())))


#row check
for i, m in enumerate(map_):
    if check(m, N, L):
        cnt += 1


for i in range(N):
    temp = []
    for j in range(N):
        temp.append(map_[j][i])
    if check(temp, N, L):
        cnt += 1

print(cnt)
