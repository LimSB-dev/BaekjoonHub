import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, int(input()) + 1):
    n, m, L = map(int, input().split())

    tree = [0] * (n + 1)

    for i in range(m):
        v1, v2 = map(int, input().split())
        tree[v1] = v2

        while v1 != 0:
            v1 //= 2
            tree[v1] += v2

    answer = tree[L]

    print(f'#{tc} {answer}')
