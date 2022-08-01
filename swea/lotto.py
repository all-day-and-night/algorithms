"""
1. 로또 번호는 중복되지 않는 숫자 6개로 구성
2. 각 번호는 1부터 45까지의 숫자로 구성
3. 로또 번호는 오름차순으로 정렬
"""


num = list(map(int, input().split()))

#1
"""
6개, 중복
"""

def solution(num):
    if len(num) != 6:
        return False
    nums = dict()
    prev = 0
    for n in num:
        # 중복
        if n in nums.keys() or (n < 1 or n > 45) or n <= prev:
            return False
        else:
            nums[n] = 1
            prev = n

    return True



print(solution(num))

