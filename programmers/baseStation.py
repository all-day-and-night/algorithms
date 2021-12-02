"""
간단한 구현 문제인데 효율성이 추가된 문제이다
굳이 deque를 사용하지 않아도 괜찮았지만 사용했다.
마지막 station의 처리를
맨 끝의 자리에 idx가 도착했을 때 닿지 않을 거리의 기지국을 임의로 넣어 예외 처리를 했다
"""
from collections import deque

def solution(n, stations, w):
    width = w * 2 + 1
    answer = 0

    stations = deque(stations)
    if stations[-1] != n:
        stations.append(n + w + 1)
    idx = 1
    now = stations.popleft()

    while idx <= n:
        if now - w > idx:
            answer += 1
            idx += width
            continue

        if now - w <= idx <= now + w:
            idx = now + w + 1
            if stations:
                now = stations.popleft()
            continue

    return answer