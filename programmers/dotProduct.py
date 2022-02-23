def solution(a, b):
    answer = sum([i * j for i, j in zip(a, b)])
    return answer