import sys
import re

input = sys.stdin.readline
T = int(input())

results = []
for _ in range(T):
    line = input().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(line)
    if m: results.append("YES")
    else: results.append("NO")

for result in results:
    print(result)