from collections import defaultdict

answer = 0


def solution(info, edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    v = [0] * len(info)
    v[0] = 1
    dfs(graph, v, info, 1, 0)
    return answer


def dfs(graph, visited, info, sheep, wolf):
    global answer

    answer = max(sheep, answer)
    if sheep <= wolf:
        return

    for i in range(len(visited)):
        if visited[i]:
            for g in graph[i]:
                if not visited[g]:
                    if info[g] == 1:
                        visited[g] = 1
                        dfs(graph, visited, info, sheep, wolf + 1)
                        visited[g] = 0
                    else:
                        visited[g] = 1
                        dfs(graph, visited, info, sheep + 1, wolf)
                        visited[g] = 0
