def solution(s):
    temp = list(map(int, s.split(' ')))
    max_ = -int(1e9)
    min_ = int(1e9)

    for t in temp:
        max_ = max(max_, t)
        min_ = min(min_, t)
    answer = str(min_) + ' ' + str(max_)
    return answer