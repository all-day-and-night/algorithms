def solution(s):
    answer = ''
    len_ = len(s)

    if len_ % 2 == 0:
        answer = s[len_ // 2 - 1: len_ // 2 + 1]
    else:
        answer = s[len_ // 2]
    print(answer)
    return answer