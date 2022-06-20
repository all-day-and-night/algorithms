"""
using stack or dfs

여러가지 방식으로 문제를 풀어보자
"""

from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

answer = int(1e9)


def compare(s1, s2):
    if len([c1 for c1, c2 in zip(s1, s2) if c1 != c2]) == 1:
        return True
    return False


def dfs(target, words, check, now, depth):
    global answer

    if now == target:
        answer = min(depth, answer)
        return

    for i in range(0, len(words)):
        if check[i] != 0:
            continue

        if compare(words[i], now):
            check[i] = 1
            dfs(target, words, check, words[i], depth + 1)
            check[i] = 0

    return


def solution(begin, target, words):
    global answer
    if target not in words:
        return 0

    check = [0] * len(words)
    dfs(target, words, check, begin, 0)

    return answer


"""def solution(begin, target, words):
    answer = 0

    # target이 존재하지 않으면 0 return
    if target not in words:
        return 0

    stack = [begin]
    check = [0] * len(words)

    while stack:
        now = stack.pop()

        if now == target:
            return answer

        for w in range(0, len(words)):
            if compare(words[w], now):
                if check[w] == 0:
                    check[w] = 1
                    stack.append(words[w])

        answer += 1

    return answer"""

"""    
def solution(begin, target, words):
    answer = 0 
    #없으면 return 0
    if target not in words:
        return 0
    check = [0 for i in words]

    stack = [begin]

    while stack:
        print(stack)
        now = stack.pop()

        if now == target:
            return answer

        for w in range(0, len(words)):
            if len([i for i in range(0, len(words[w])) if words[w][i] != now[i]]) == 1:
                if check[w] != 0:
                    continue

                check[w] = 1
                stack.append(words[w])
        answer += 1


    return answer"""