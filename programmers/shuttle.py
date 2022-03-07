from collections import deque

"""
def solution(n, t, m, timetable):
    answer = ''
    start = 9 * 60
    table = deque()
    for time in timetable:
        hh, mm = map(int, time.split(':'))
        table.append(hh * 60 + mm)
    table = deque(sorted(table))
    end = start + (n-1) * t

    for i in range(n):
        now = start + i * t
        if i == n-1:
            temp = [i for i in table if i <= now]
            if len(temp) >= m:
                answer = temp[m-1] - 1
            else:
                if 0 < len(temp) < m:
                    answer = now
                else:
                    answer = now

        for j in range(m):
            if table and table[0] <= now:
                table.popleft()

    hh = answer // 60
    mm = answer % 60
    answer = "%02d:%02d"%(hh, mm)
    return answer"""


def getTime(time):
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)


def getString(value):
    hh = value // 60
    mm = value % 60
    return "%02d:%02d" % (hh, mm)


def solution(n, t, m, timetable):
    table = []
    for time in timetable:
        table.append(getTime(time))

    table.sort()

    start = getTime("09:00")

    end = start + t * (n - 1)

    q = deque(table)

    for i in range(n - 1):
        checkPoint = start + (t * i)
        for j in range(m):
            if q and q[0] <= checkPoint:
                q.popleft()

    cand = [i for i in q if i <= end]

    if len(cand) >= m:
        return getString(cand[m - 1] - 1)
    else:
        return getString(end)