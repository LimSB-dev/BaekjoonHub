import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    answer = 0

    # 위치 변경
    for i in range(1, n + 1):
        while arr[i//2] > arr[i]:
            arr[i//2], arr[i] = arr[i], arr[i//2]
            i //= 2

    # 부모 노드 합
    while n != 0:
        n //= 2
        answer += arr[n]

    print(f'#{tc} {answer}')
