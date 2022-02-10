month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

day = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}


def solution(a, b):
    answer = ''

    sum_ = 0
    for i in range(1, a):
        sum_ += month[i]

    sum_ += b - 1

    sum_ %= 7

    answer = day[sum_]

    return answer