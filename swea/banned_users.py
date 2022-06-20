from itertools import permutations

def check(users, banned_id):
    for user, banned in zip(users, banned_id):
        if len(user) != len(banned):
            return False

        for u, b in zip(user, banned):
            if b == '*':
                continue
            if u != b:
                return False

    return True

def solution(user_id, banned_id):

    banned_set = []

    for users in permutations(user_id, len(banned_id)):
        if check(users, banned_id):
            user_set = set(users)
            if user_set not in banned_set:
                banned_set.append(user_set)

    return len(banned_set)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

print(solution(user_id, banned_id))