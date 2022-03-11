"""
구명 보트 문제는 최대 2명만 태울 수 있는 조건이 있기 때문에

약간 변형하여 limit을 넘지 않는다면 계속 태울 수 있는 조건으로 문제를 해결하였다.
"""

def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people) - 1

    temp = people[end]
    while start < end:
        print(start, end)
        if temp + people[start] <= limit:
            temp += people[start]
            start += 1

        elif temp + people[start] > limit:
            answer += 1
            end -= 1
            temp = people[end]

    if temp <= limit:
        answer += 1

    print(answer)

people = [70, 50, 80]
limit = 100
solution(people, limit)
