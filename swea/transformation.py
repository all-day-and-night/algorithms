def is_balanced(p):
    u = ""
    cnt = 0
    for i, c in enumerate(p):
        if c == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return p[:i+1], p[i+1:]

def is_right(p):
    stack = []

    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return True

def solution(p):
    #1
    if len(p) == 0:
        return ""

    #2
    u, v = is_balanced(p)

    #3
    if is_right(u):
        return u + solution(v)
    #4
    else:
        reverse_u = ['(' if c == ')' else ')' for c in u[1:-1]]

        return '(' + solution(v) + ')' + ''.join(reverse_u)

s = "()))((()"
print(solution(s))

