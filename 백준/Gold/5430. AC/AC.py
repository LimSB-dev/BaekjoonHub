import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    
    reverse = False
    count_d = p.count('D')

    if count_d > n:
        print('error')
        continue

    if n == 0:
        arr = deque()
    
    for operator in p:
        if operator == 'R':
            reverse = not reverse
        elif operator == 'D':
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if reverse:
        arr.reverse()

    print('[' + ','.join(arr) + ']')