def sol(a, b):
    dist = b - a
    cnt = 0 # 이동 횟수
    move = 1 # cnt 별 빈도수
    move_plus = 0 # 이동한 거리의 합
    while move_plus < dist:
        cnt += 1
        move_plus += move
        if cnt % 2 == 0:
            move += 1
    return cnt

N = int(input())
result = []
for _ in range(N):
    a, b = map(int, input().split())
    result.append(sol(a, b))

for r in result:
    print(r)
