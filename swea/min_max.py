"""
비효율적이지만 짧게 줄이는 거 생각보다 재밌네
"""

def solution(s):
    return str(min(list(map(int, s.split())))) + " " + str(max(list(map(int, s.split()))))
