def solution(d, budget):
    answer = 0
    d.sort()
    len_ = len(d)
    sum_ = sum(d)

    for i in range(len_ - 1, -1, -1):
        if sum_ <= budget:
            answer = i + 1
            break
        sum_ = sum_ - d[i]

    return answer