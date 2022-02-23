def solution(a, b):
    start = min(a, b)
    end = max(a, b)
    return sum([i for i in range(start, end+1)])