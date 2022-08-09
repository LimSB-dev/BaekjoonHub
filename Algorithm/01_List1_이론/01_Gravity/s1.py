import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    max_height = arr[0]

    for i in range(n):
        # 중력 크기를 담을 변수 gravity에 초기값 0을 할당한다.
        gravity = 0

        # 만약 index가 i인 상자의 높이가 현재 최대 높이보다 높다면 max_height에 li[i]를 대입시킨다.
        # 오른쪽 상자의 높이가 이전의 가장 높은 상자에 비해 낮다면 굳이 탐색할 필요가 없다.
        if max_height <= arr[i]:
            max_height = arr[i]

            # 오른쪽 상자부터 끝까지 탐색한다.
            for j in range(i + 1, n):

                # 만약 i index의 상자가 j index 상자보다 높다면 아래로 낙하하기 때문에 gravity가 1 증가한다.
                if arr[i] > arr[j]:
                    gravity += 1

                # 만약 gravity 크기가 answer보다 크다면 answer에 gravity 대입
                if gravity > answer:
                    answer = gravity

    print(f'#{tc} {answer}')