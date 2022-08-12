import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 1
    max_value = 1
    n = int(input())
    numbers = list(map(int, input().split()))
    pre_num = numbers[0]

    for number in numbers:
        if number > pre_num:
            answer += 1
            pre_num = number
            if max_value < answer:
                max_value = answer
        else:
            pre_num = number
            answer = 1

    print(f'#{tc} {max_value}')
