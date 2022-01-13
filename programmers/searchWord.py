"""
2가지 방법으로 문제를 풀음
하나는 이분탐색을 활용하였고
하나는 Trie 구조를 활용했다

이분탐색도 좋지만 문자열 검색 등에는 Trie 구조를 사용하는 것이 좋을 것 같다.
"""

"""
1. 이분 탐색 사용
"""

from bisect import bisect_left, bisect_right


def count_by_range(a, left, right):
    left_index = bisect_left(a, left)
    right_index = bisect_right(a, right)
    return right_index - left_index


def solution1(words, queries):
    answer = []
    index = [[] for _ in range(10001)]
    reverse = [[] for _ in range(10001)]

    for word in words:
        index[len(word)].append(word)
        reverse[len(word)].append(word[::-1])

    for i in range(10001):
        index[i].sort()
        reverse[i].sort()

    for query in queries:
        if query[0] != '?':
            ans = count_by_range(index[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            ans = count_by_range(reverse[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(ans)
    return answer

"""
2. Trie 구초 사용
"""


class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}


class Trie(object):
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

    def start_with(self, prefix):
        cur_node = self.head
        result = 0

        for char in prefix:
            if char == "?":
                break
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return 0
        return cur_node.count


def solution(words, queries):
    answer = []
    tries = {}
    reverses = {}

    for word in words:
        if len(word) in tries:
            tries[len(word)].insert(word)
            reverses[len(word)].insert(word[::-1])
        else:
            trie = Trie()
            reverse = Trie()

            trie.insert(word)
            reverse.insert(word[::-1])

            tries[len(word)] = trie
            reverses[len(word)] = reverse

    for query in queries:
        if len(query) in tries:
            if query[0] != '?':
                answer.append(tries[len(query)].start_with(query))
            else:
                answer.append(reverses[len(query)].start_with(query[::-1]))
        else:
            answer.append(0)
    return answer