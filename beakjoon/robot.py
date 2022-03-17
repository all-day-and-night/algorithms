from collections import deque

N, K = map(int, input().split())

data = list(map(int, input().split()))

def get_idx(idx, i):
    return (idx + i + N * 2) % (N * 2)

def print_data(idx):
    for i in range(N * 2):
        print(data[get_idx(idx, i)], end = ' ')
    print()
idx = 0

robots = [0] * (N*2)
robots_idx = deque()
cnt = data.count(0)

answer = 0
while cnt < K:
    #한칸 회전
    idx -= 1
    if robots[get_idx(idx, N-1)] == 1:
        robots[get_idx(idx, N-1)] = 0

    #로봇 이동
    for i in range(N-1, -N-1 , -1):
        if robots[get_idx(idx, i)] == 1 and robots[get_idx(idx, i+1)] == 0 and data[get_idx(idx, i+1)] > 0:
            robots[get_idx(idx, i)] = 0
            data[get_idx(idx, i + 1)] -= 1
            if data[get_idx(idx, i+1)] == 0:
                cnt += 1
            if i + 1 != N-1:
                robots[get_idx(idx, i+1)] = 1

    #로봇 올리기
    if data[get_idx(idx, 0)] > 0:
        robots[get_idx(idx, 0)] = 1
        data[get_idx(idx, 0)] -= 1
        if data[get_idx(idx, 0)] == 0:
            cnt += 1

    answer += 1
print(answer)


