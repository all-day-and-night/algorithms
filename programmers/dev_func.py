import math


def solution(progresses, speeds):
    days = []
    for pro, speed in zip(progresses, speeds):
        if len(days) == 0 or days[-1][0] < math.ceil((100 - pro) / speed):
            days.append([math.ceil((100 - pro) / speed), 1])
        else:
            days[-1][1] += 1

    answer = [i[1] for i in days]
    return answer
