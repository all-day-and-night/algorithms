def sticky_sol(servers, requests):
    answer = [[] for _ in range(servers)]
    idx = 0
    maps = {}
    for request in requests:
        if request in maps.keys():
            answer[maps[request]].append(request)
        else:
            answer[idx].append(request)
            maps[request] = idx
            idx = (idx + 1) % servers

    return answer


def sol(servers, requests):
    answer = [[] for _ in range(servers)]
    idx = -1
    for request in requests:
        idx = (idx + 1) % servers
        answer[idx].append(request)

    return answer


def solution(servers, sticky, requests):
    answer = []
    if sticky:
        answer = sticky_sol(servers, requests)
    else:
        answer = sol(servers, requests)
    print(answer)
    return answer

servers = 2
sticky = True
requests = [1, 2, 2, 3, 4, 1]

solution(servers, sticky, requests)

