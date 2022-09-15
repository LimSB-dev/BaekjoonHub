import sys
sys.stdin = open('input.txt', encoding='utf-8')

operators = ['+', '-', '*', '/']


def cal_num(node):
    if node != 0:
        if tree[node] in operators:
            a = cal_num(ch1[node])
            b = cal_num(ch2[node])
            if tree[node] == '+':
                result = a + b
            elif tree[node] == '-':
                result = a - b
            elif tree[node] == '*':
                result = a * b
            elif tree[node] == '/':
                result = a / b
            return result
        else:
            return int(tree[node])


for tc in range(1, 11):
    n = int(input())
    tree = [''] * (n + 1)
    answer = 0

    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    # tree 채우기
    for i in range(1, n + 1):
        arr = list(map(str, input().split()))

        # Leaf Node
        if len(arr) == 2:
            tree[i] = arr[1]
            ch1[int(arr[0])] = 0
            ch2[int(arr[0])] = 0
        else:
            tree[i] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])

    answer = cal_num(1)

    print(f'#{tc} {int(answer)}')
