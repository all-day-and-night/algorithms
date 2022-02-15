"""
parametric search -> 이분탐색과 유사한데 값의 범위를 찾아 최적의 해를 찾는 것

비슷한 문제를 풀어본 경험이 있지만, 구현하는데 어려움을 겪음

효율성의 문제일 경우 생각해야할 경우의 수가 늘어났다....
"""

def solution(n, cores):
    answer = 0

    if len(cores) >= n:
        return n

    n -= len(cores)

    left = 1
    right = n * max(cores)

    while left < right:

        mid = (left + right) // 2

        cnt = 0
        for core in cores:
            cnt += mid // core

        if cnt >= n:
            right = mid
        else:
            left = mid + 1

    print(right)
    for core in cores:
        n -= (right - 1) // core

    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1

    return answer

