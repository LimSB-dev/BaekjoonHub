import sys
sys.stdin = open('input.txt', encoding='utf-8')


# 중위 순회 (L -> V -> R)
def in_order(node):
    global arr, value
    if node != 0:
        in_order(ch1[node])
        arr[node] = value
        value += 1
        in_order(ch2[node])


for tc in range(1, int(input()) + 1):
    n = int(input())                        # 정점의 개수
    arr = [0] * (n + 1)                     # 저장된 값
    value = 1

    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    for i in range(1, (n // 2) + 1):
        if i * 2 <= n:
            ch1[i] = i * 2
            if (i * 2) + 1 <= n:
                ch2[i] = (i * 2) + 1

    in_order(1)

    root = arr[1]                           # 루트 노드
    answer = arr[n//2]                      # N//2번 노드에 저장된 값

    print(f'#{tc} {root} {answer}')
