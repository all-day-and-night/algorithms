"""
사전순 부분 문자열

이거 알아두면 편할 듯 ㄹㅇ


"""

def solution(s):
    stack = []

    for c in s:
        while stack and stack[-1] < c:
            stack.pop()
        stack.append(c)
    return ''.join(stack)

print(solution("yxyc"))
