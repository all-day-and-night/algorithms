def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        elif i.islower():
            temp = ((ord(i) + n) - ord('a')) % 26 + ord('a')
            answer += chr(temp)
        elif i.isupper():
            temp = ((ord(i) + n) - ord('A')) % 26 + ord('A')
            answer += chr(temp)

    return answer