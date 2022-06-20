"""
물론 brute force로 모두 찾으면 되지만

투포인터 써서 해결해봄

한동안 굳어 있었으니까

얼른 다시 뇌 돌리자
"""

def solution(n):
    answer = 0
    cnt = 1
    left = 1
    right = 1
    sum_ = 1

    while right < n:
        if sum_ < n:
            right += 1
            sum_ += right

        elif sum_ > n:
            sum_ -= left
            left += 1

        elif sum_ == n:
            cnt += 1
            sum_ -= left
            left += 1

    return cnt

solution(15)