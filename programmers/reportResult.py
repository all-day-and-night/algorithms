"""
반년 전에 봤던 카카오 코테 문제인데
이렇게 쉬운 문제를 얼마나 붙잡고 있었던지 한이 사무친다
이번에 코테 부순다
"""

def solution(id_list, report, k):
    answer = []
    from_list = {}
    to_list = {}
    for Id in id_list:
        from_list[Id] = set()
        to_list[Id] = 0

    for t in report:
        a, b = t.split()
        if a not in from_list[b]:
            from_list[b].add(a)

    for Id in id_list:
        if len(from_list[Id]) >= k:
            for to in from_list[Id]:
                to_list[to] += 1

    for Id in id_list:
        answer.append(to_list[Id])

    return answer