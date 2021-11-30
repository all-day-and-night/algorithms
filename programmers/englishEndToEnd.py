def check1(words, n):
    len_ = len(words)
    prev = words[0]
    for i in range(1, len_):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            return [i % n + 1, i // n + 1]

    return [0, 0]


def solution(n, words):
    return check1(words, n)