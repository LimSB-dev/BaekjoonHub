import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_node(num):
    if num != 0:
        global answer
        answer += 1
        find_node(ch1[num - 1])
        find_node(ch2[num - 1])


for tc in range(1, int(input()) + 1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0

    ch1 = [0] * (e + 1)
    ch2 = [0] * (e + 1)

    for i in range(e):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]

        if ch1[v1 - 1] == 0:
            ch1[v1 - 1] = v2
        else:
            ch2[v1 - 1] = v2

    find_node(n)

    print(f'#{tc} {answer}')
