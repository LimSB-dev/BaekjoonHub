import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = [0] * 10
    arr = list(map(int, input().split()))
    
    # 버블 정렬을 사용해 arr를 정렬
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # answer 리스트에 특별한 정렬 10회
    for i in range(10):
        # 홀수라면 오름차순
        if i % 2 != 0:
            answer[i] = arr[i//2]
        # 짝수라면 내림차순
        else:
            answer[i] = arr[(n-1) - i//2]
    
    print(f'#{tc}', end=' ')
    print(*answer)
