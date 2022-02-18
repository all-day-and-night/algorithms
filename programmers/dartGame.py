def solution(dartResult):
    answer = 0

    stack = []
    digit = ""
    for d in dartResult:
        if d.isdigit():
            digit += d

        else:
            if d == 'S':
                stack.append(int(digit))
                digit = ""
            elif d == 'D':
                stack.append(int(digit) ** 2)
                digit = ""
            elif d == 'T':
                stack.append(int(digit) ** 3)
                digit = ""

            else:
                if d == '*':
                    if len(stack) > 1:
                        stack[-1] *= 2
                        stack[-2] *= 2
                    else:
                        stack[-1] *= 2
                if d == '#':
                    stack[-1] *= -1
    answer = sum(stack)
    return answer