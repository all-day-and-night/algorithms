def solution(s):
    isFirst = True
    answer = ""
    for i in s:
        if i == " ":
            answer += i
            isFirst = True
            continue
        if isFirst:
            answer += i.upper()
            isFirst = False
        else:
            answer += i.lower()

    return answer