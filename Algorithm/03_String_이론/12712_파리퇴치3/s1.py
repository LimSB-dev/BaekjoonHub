import sys
sys.stdin = open('input.txt')

t = int(input())

arr = list(range(1, 13))

for tc in range(1, t + 1):
    answer = 0
    # n: 부분집합 원소의 수
    # k: 부분집합의 합
    n, k = map(int, input().split())
    
    for i in range(1 << 12):
        cnt = 0
        sum_of_subset = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                sum_of_subset += arr[j]
    
        if cnt == n and sum_of_subset == k:
            answer += 1
            
    print(f'#{tc} {answer}')
