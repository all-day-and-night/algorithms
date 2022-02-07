class Node:
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for char in string:
            cur_node.count += 1

            if char not in cur_node.children:
                cur_node.children[char] = Node(char)

            cur_node = cur_node.children[char]

        cur_node.count += 1

    def search(self, word):
        cur_node = self.head
        result = 0

        for char in word:
            if char in cur_node.children:
                if cur_node.count == 1:
                    return result
                result += 1
                cur_node = cur_node.children[char]
        return result


def solution(words):
    answer = 0
    db = Trie()

    for word in words:
        db.insert(word)

    for word in words:
        answer += db.search(word)

    return answer