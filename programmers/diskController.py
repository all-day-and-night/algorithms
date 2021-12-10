#using sort
"""
import heapq

def solution(jobs):
    answer = 0
    q = []
    ms = 0
    len_ = len(jobs)
    jobs.sort(key=lambda x: x[1]) # execute_time으로 오름차순
    print(jobs)

    while len(jobs) > 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= ms:
                ms += jobs[i][1]
                answer += (ms - jobs[i][0])
                jobs.pop(i)
                break
            if i == len(jobs)-1:
                ms += 1

    result = (answer // len_)

    return result
"""
#using heapq
import heapq
from collections import deque


def solution(jobs):
    stack = []
    answer = []
    len_ = len(jobs)
    jobs.sort(key=lambda x: x[0])
    jobs = deque(jobs)
    ms = 0
    while jobs:
        while jobs and jobs[0][0] <= ms:
            start, end = jobs.popleft()
            heapq.heappush(stack, [end, start])

        if stack:
            end, start = heapq.heappop(stack)
            ms += end
            answer.append(ms - start)
        else:
            ms += 1

    while stack:
        end, start = heapq.heappop(stack)
        ms += end
        answer.append(ms - start)

    return sum(answer) // len_