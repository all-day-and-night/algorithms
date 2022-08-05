from collections import defaultdict


def check(window, want_set):
    for key, value in want_set.items():
        if key not in window.keys():
            return False

        if window[key] != want_set[key]:
            return False
    return True


def solution(want, number, discount):
    answer = 0

    want_set = {}
    for w, cnt in zip(want, number):
        want_set[w] = cnt

    window = {}
    for i in range(10):
        if discount[i] in window.keys():
            window[discount[i]] += 1
        else:
            window[discount[i]] = 1

    days = len(discount)

    for i in range(days - 10):
        if check(window, want_set):
            answer += 1

        window[discount[i]] -= 1
        if window[discount[i]] == 0:
            del window[discount[i]]

        if discount[i + 10] in window.keys():
            window[discount[i + 10]] += 1
        else:
            window[discount[i + 10]] = 1

    return answer

want = ["banana", "apple", "rice","pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]


print(solution(want, number, discount))