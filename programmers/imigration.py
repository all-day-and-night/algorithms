"""def solution(n, times):
    max_ = max(times) * n
    answer = -1
    left = 1
    right = max_

    while left < right:
        mid = (left+right) // 2

        total = 0
        for t in times:
            total += mid // t
            if total >= n:
                break

        if total >= n:
            answer = mid
            right = mid

        else:
            left = mid + 1

    print(left, right)
    return answer"""

"""
def solution(n, times):
    answer = 0
    left = 0
    max_ = max(times) * n
    right = max_

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for t in times:
            total += mid // t
            if total>=n:
                break

        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)
    return answer
"""


def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for time in times:
            cnt += mid // time

            if cnt >= n:
                break
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


