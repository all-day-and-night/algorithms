def solution(participant, completion):
    answer = ''
    comp = {}

    for com in completion:
        if com not in comp.keys():
            comp[com] = 1
        else:
            comp[com] += 1

    for part in participant:
        if part not in comp.keys():
            return part
        if part in comp.keys():
            comp[part] -= 1
            if comp[part] == 0:
                del comp[part]

    return answer