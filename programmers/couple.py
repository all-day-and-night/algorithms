def solution(s):
    q = []

    for i in s:
        if q and q[-1] == i:
            q.pop()
        else:
            q.append(i)

    return 1 if len(q) == 0 else 0


"""
from collections import deque

def solution(s):
    q = []
    s = deque(s)

    while s:

        temp = s.popleft()
        if len(q) == 0:
            q.append(temp)
        else:
            if q[-1] == temp:
                q.pop()
            else:
                q.append(temp)

    if len(q) == 0:
        return 1
    else:
        return 0"""