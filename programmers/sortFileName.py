#단순 정렬 문제
#문자열을 어떤식으로 split 할지가 중요한데
#무식하게 하나씩 비교해서 head, number, tail을 나눔
#다른 코드랑 비교해보는 것도 좋을 것 같다.

def fileSplit(file):
    head = ""
    temp = list(file[::-1])
    # head
    while temp:
        if temp[-1].isdigit():
            break
        else:
            head += temp.pop()

    # Number
    number = ""
    while temp:
        if temp[-1].isdigit():
            number += temp.pop()
        else:
            break

    head = head.lower()
    number = int(number)

    if len(temp) == 0:
        return head, number, ""

    tail = ''.join(temp[::-1])
    if tail[0] == ' ':
        tail = tail[1:]

    return head, number, tail


def solution(files):
    answer = []
    dict_ = dict()
    for i, file in enumerate(files):
        head, number, tail = fileSplit(file)
        dict_[file] = [head, number, i, tail]

    sorted_ = sorted(dict_.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]))
    answer = [key for key, value in sorted_]

    return answer