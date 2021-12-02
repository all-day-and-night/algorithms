#그래프 순환으로 푸는 문제라고 생각했지만
#간단하게 set을 사용한 풀이가 가능하다.
#간단하게 풀 수 있는 방법을 먼저 고려하고 시작해보자

def solution(dirs):
    answer = 0
    temp = set()
    dir_ = {'U': (1, 0), 'R': (0, 1), 'D': (-1, 0), 'L': (0, -1)}
    x, y = 0, 0
    for d in dirs:
        nx, ny = x + dir_[d][0], y + dir_[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            temp.add((x, y, nx, ny))
            temp.add((nx, ny, x, y))
            x, y = nx, ny

    return len(temp) // 2