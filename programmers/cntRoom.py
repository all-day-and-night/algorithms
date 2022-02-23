"""
union find 문제

이 문제에서는 이동한 노드가 이전에 방문했을 경우 사이클이 형성되기 때문에 answer를 ++ 한다

유니온 파인트를 쓰지 않고 풀 수 있다.

defaultdict을 사용하여 키를 처음에 넣으면 0으로 초기화되고

defalutdict에 키가 존재한다면 이미 방문했기 때문에

answer를 +한다

이 때 노드끼리 겹치지 않고 사이클이 형성될 수 있기 때문에 한번에 2번씩 이동하여 문제를 해결한다

또한 방향도 중요하기 때문에 한번 이동한 경로를 저장하는 defaultdict을 하나 추가하여 실행한다.
"""

from collections import defaultdict, deque

def solution(arrows):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    x, y = 0, 0
    visited = defaultdict(int)
    visited_dir = defaultdict(int)

    q = deque()
    q.append((x, y))
    for i in arrows:
        for _ in range(2):
            nx, ny = x + dx[i], y + dy[i]
            q.append([nx, ny])
            x, y = nx, ny

    x, y = q.popleft()
    visited[(x, y)] = 1
    cnt = 0
    while q:
        nx, ny = q.popleft()

        if visited[(nx, ny)] == 1:
            if visited_dir[((x, y), (nx, ny))] == 0:
                cnt += 1
        else:
            visited[(nx, ny)] = 1

        visited_dir[((x, y), (nx, ny))] = 1
        visited_dir[((nx, ny), (x, y))] = 1
        x, y = nx, ny

    return cnt



arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))