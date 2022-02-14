def solution(absolutes, signs):
    answer = 0

    for value, sign in zip(absolutes, signs):
        if sign:
            answer += value
        else:
            answer -= value
    return answer