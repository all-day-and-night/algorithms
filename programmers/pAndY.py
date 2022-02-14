def solution(s):
    answer = True

    cnt = 0
    for key in s:
        temp = key.lower()
        if temp == 'p':
            cnt += 1
        elif temp == 'y':
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False