import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))

    # [idx, vlaue] 인 큐
    queue = []
    for idx, value in enumerate(q):
        queue.append([idx, value])

    answer = []

    for _ in range(n):
        answer.append(queue.pop(0))

    while len(answer) > 1:
        # 입구의 피자 확인
        pizza = answer.pop(0)
        idx = pizza[0]
        num = pizza[1]

        # 치즈가 녹는 중
        num //= 2

        # 치즈가 다 구워지면 빼준다.
        if num == 0:
            # q가 비어있지 않다면 새로운 피자를 채워준다.
            if queue:
                answer.append(queue.pop(0))
        # 치즈가 구워지지 않으면 다시 화덕에 넣어준다.
        else:
            answer.append([idx, num])

    print(f'#{tc} {answer.pop(0)[0] + 1}')
