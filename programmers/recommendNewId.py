from collections import deque

isCan = set(['-', '_', '.'])


def solution(new_id):
    answer = ""
    isCan = set(['-', '_', '.'])

    for new in new_id:
        if new.isdigit():
            answer += new
        elif new.isalpha():
            answer += new.lower()

        else:
            if new in isCan:
                if new == '.' and len(answer) > 0 and answer[-1] == '.':
                    continue
                answer += new
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]

    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    if not answer:
        answer = "a"

    if len(answer) > 15:
        answer = answer[:15]

    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    while len(answer) < 3:
        answer += answer[-1]

    return answer