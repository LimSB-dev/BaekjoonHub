import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    q = list(map(int, input().split()))

    # 0 이하의 값이 나올 때까지 반복
    while q[-1] != 0:

        # 사이클
        for i in range(1, 6):
            num = q[0]
            q = q[1:]
            num -= i
            q.append(num)

            # 종료 조건
            if num <= 0:
                q[-1] = 0
                break

    print(f'#{tc}', *q)
