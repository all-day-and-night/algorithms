import sys

input = sys.stdin.readline

T = int(input())

def compare(x, y, nx, ny):
    if x < nx or y < ny:
        return True
    return False

answer = []
for _ in range(T):
    N = int(input())

    score = []
    INF = int(1e9)

    for _ in range(N):
        a, b = map(int, input().split())
        score.append([a, b])

    score.sort(key=lambda x: x[0])

    cnt = 0

    min_rank = score[0][1]

    for s in score:
        if min_rank >= s[1]:
            cnt += 1
            min_rank = s[1]
    answer.append(cnt)


for ans in answer:
    print(ans)