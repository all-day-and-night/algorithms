from collections import deque

class Node:
    def __init__(self, value, cnt):
        self.value = value
        self.child = {}
        self.childNum = 0
        self.cnt = cnt

class Trie:
    def __init__(self):
        self.head = Node(None, 0)

    def insert(self, q):
        cur = self.head
        cnt = 0
        while q:
            now = q.popleft()
            if now not in cur.child.keys():
                cur.child[now] = Node(now, cnt)
                cur.childNum += 1

            cnt += 2
            cur = cur.child[now]

    def printNode(self, cur):
        if cur.value != None:
            print('-' * cur.cnt + str(cur.value))

        if cur.childNum == 0:
            return

        nexts = sorted(list(cur.child.keys()))
        for n in nexts:
            self.printNode(cur.child[n])



N = int(input())

head = Node(Node, 0)
trie = Trie()

for _ in range(N):
    temp = list(input().split())
    q = deque(temp[1:])
    trie.insert(q)

trie.printNode(trie.head)



