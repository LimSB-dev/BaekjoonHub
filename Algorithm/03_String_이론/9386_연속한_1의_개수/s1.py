import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = input()
    max_value = 0
    cnt = 0
    for i in numbers:
        if i == '1':
            cnt += 1
            if max_value < cnt:
                max_value = cnt
        else:
            cnt = 0
    print(f'#{tc} {max_value}')