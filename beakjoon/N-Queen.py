from itertools import permutations

N = int(input())

col = [-1] * N
cnt = 0

def check(now):
    if now == 0:
        return True
    for i in range(now):
        if col[i] == col[now] or col[i] + i == col[now] + now or col[i] - i == col[now] -now:
            return False
    return True


def queen(now):
    global cnt
    if now == N:
        cnt += 1
        return

    for i in range(N):
        col[now] = i
        if check(now):
            queen(now+1)

queen(0)
print(cnt)
