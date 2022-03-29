from collections import defaultdict

N = int(input())

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = {}

for _ in range(N):
    root, left, right = input().split()
    if root not in tree:
        tree[root] = Node(root)

    if left != '.' and left not in tree:
        tree[left] = Node(left)

    if right != '.' and right not in tree:
        tree[right] = Node(right)

    if left != '.':
        tree[root].left = left

    if right != '.':
        tree[root].right = right



def pre_order(tree, root):
    if root not in tree:
        return

    print(tree[root].value, end='')
    pre_order(tree, tree[root].left)
    pre_order(tree, tree[root].right)


def in_order(tree, root):
    if root not in tree:
        return

    in_order(tree, tree[root].left)
    print(tree[root].value, end='')
    in_order(tree, tree[root].right)


def post_order(tree, root):
    if root not in tree:
        return

    post_order(tree, tree[root].left)
    post_order(tree, tree[root].right)
    print(tree[root].value, end='')

pre_order(tree, 'A')
print()
in_order(tree, 'A')
print()
post_order(tree, 'A')

