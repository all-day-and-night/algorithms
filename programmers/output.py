from collections import deque


class Node:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
        self.child = {}
        self.parent = None


def dfs(teams, mng, choose, value):
    if not mng:
        print(choose)
        print(value)
        return value

    now = list(mng)[0]

    # parent만 제거
    mng.remove(now)
    choose.add(now)
    dfs(teams, mng, choose, value + teams[now].value)
    mng.add(now)
    if now in choose:
        choose.remove(now)

    # parent 말고 child 선택
    mng.remove(now)
    for child in teams[now].child.keys():
        isExist = False
        if child in mng:
            isExist = True
            mng.remove(child)
        choose.add(child)
        dfs(teams, mng, choose, value + teams[child].value)
        if isExist:
            mng.add(child)
        choose.remove(child)
    mng.add(now)


def solution(sales, links):
    answer = 0

    teams = [Node(i, sale) for i, sale in enumerate(sales)]
    check = [0 for _ in range(len(sales))]

    for a, b in links:
        teams[a - 1].child[b - 1] = teams[b - 1]
        teams[b - 1].parent = teams[a - 1]

    mng = set()
    for node in teams:
        if len(node.child) > 0:
            mng.add(node.ID)
    choose = set()
    dfs(teams, mng, choose, 0)

    return answer

sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
solution(sales, links)