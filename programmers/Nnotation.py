def intToStr(value, notation):
    if value == 10:
        return 'A'
    elif value == 11:
        return 'B'
    elif value == 12:
        return 'C'
    elif value == 13:
        return 'D'
    elif value == 14:
        return 'E'
    elif value == 15:
        return 'F'
    else:
        return str(value)


def intToNotation(value, notation):
    value[0] = value[0] + 1
    len_ = len(value)
    for i in range(len_):
        if value[i] >= notation:
            if i == len_ - 1:
                value.append(0)
            value[i + 1] += 1
            value[i] = ((value[i]) % notation)
        else:
            break
    return value



# 진법, 미리 구할 숫자의 개수, 참가 인원, 튜브의 순서
def solution(n, t, m, p):
    # answer = ''
    s = ""
    now = [0]
    idx = 0
    answer = []
    while len(answer) < t:
        q = now.copy()
        while q:
            k = q.pop()
            if idx == p - 1:
                answer.append(intToStr(k, n))
            idx = (idx + 1) % m

        now = intToNotation(now, n)

    return ''.join(answer[:t])