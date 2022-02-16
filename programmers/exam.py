def solution(answers):
    answer = []
    math1_ = [1, 2, 3, 4, 5]
    math2_ = [2, 1, 2, 3, 2, 4, 2, 5]
    math3_ = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    len_ = len(answers)

    math1 = math1_ * (len_ // len(math1_)) + math1_[:len_ % len(math1_)]
    math2 = math2_ * (len_ // len(math2_)) + math2_[:len_ % len(math2_)]
    math3 = math3_ * (len_ // len(math3_)) + math3_[:len_ % len(math3_)]

    cnts = [0, 0, 0]
    for i in range(len_):
        if math1[i] == answers[i]:
            cnts[0] += 1
        if math2[i] == answers[i]:
            cnts[1] += 1
        if math3[i] == answers[i]:
            cnts[2] += 1

    max_ = max(cnts)
    for i in range(3):
        if cnts[i] == max_:
            answer.append(i + 1)

    return answer