import sys
sys.stdin = open("input.txt")


# 부분집합의 합을 구하는 함수
def sum_of_subset(arr):
    # 부분집합의 합이 하나라도 0이람면 1로 바뀌고 반복문 탈출
    answer = 0
    # 1 >> 10 은 비트 연산자로 2진법 상태에서 1을 10칸 이동 시켜주는것을 의미한다.
    # 0000 0000 0001 ( 1 ) -> 0100 0000 0000 ( 2^10 )
    for i in range(1 << 10):
        # 부분집합의 합을 담을 변수
        subset = 0
        for j in range(10):
            # & 는 AND를 찾는 비트연산자로, 2진수 형태에서 공통된 값을 10 진수로 변환해 리턴해주는 역할
            # i와 (1 << j) 가 같은게 있다면 0이 아니기 때문에 True로 if 문이 실행됩니다.
            if i & (1 << j):
                subset += arr[j]

                # 부분집합의 합이 0이라면 answer 값에 1을 대입후 반복문 탈출
                if not subset:
                    answer = 1
                    print(i, j)
                    break
        if answer:
            break
    return answer


t = int(input())

for tc in range(1, t + 1):
    numbers = list(map(int, input().split()))

    print(f'#{tc} {sum_of_subset(numbers)}')
