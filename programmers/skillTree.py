from collections import defaultdict


def sol(orders, s):
    now = -1

    for i in s:
        if i not in orders.keys():
            continue

        if orders[i] != now + 1:
            return False

        now = orders[i]

    return True


def solution(skill, skill_trees):
    answer = 0

    orders = defaultdict(int)

    for i, s in enumerate(skill):
        orders[s] = i

    for s in skill_trees:
        if sol(orders, s):
            answer += 1

    return answer