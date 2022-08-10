import sys
sys.stdin = open("input.txt")


def sum_of_subset(arr):
    answer = 0
    for i in range(1 << 10):
        subset = 0
        for j in range(10):
            if i & (1 << j):
                subset += arr[j]

                if not subset:
                    answer = 1
                    break
        if answer:
            break
    return answer


t = int(input())

for tc in range(1, t + 1):
    numbers = list(map(int, input().split()))

    print(f'#{tc} {sum_of_subset(numbers)}')
