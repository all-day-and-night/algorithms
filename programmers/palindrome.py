def solution(s):
    answer = 0
    for i in range(0, len(s)):
        start = i - 1
        end = i + 1
        # 짝수일 경우
        if end < len(s) and s[i] == s[end]:
            start = i
            end = i + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    start -= 1
                    end += 1
                else:
                    break
            answer = max(answer, len(s[start + 1:end]))

        # 범위 확인
        # 짝수일 때, 홀수일 때 다르게 생각해야함
        start = i - 1
        end = i + 1
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
            # 양 끝이 다를 경우 break
            else:
                break
        answer = max(answer, len(s[start + 1:end]))

    return answer



