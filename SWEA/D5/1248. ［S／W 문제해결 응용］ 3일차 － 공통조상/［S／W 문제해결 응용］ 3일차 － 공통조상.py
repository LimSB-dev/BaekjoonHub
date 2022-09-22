def find_node(num_1, num_2):
    nodes_1 = set()
    nodes_2 = set()

    while True:
        nodes_1.add(num_1)

        if num_1 in nodes_2:
            return num_1

        num_1 = par[num_1]

        nodes_2.add(num_2)

        if num_2 in nodes_1:
            return num_2

        num_2 = par[num_2]


def find_sub(num):
    global answer

    if ch2[num] != 0:
        answer += 1
        find_sub(ch2[num])

    if ch1[num] != 0:
        answer += 1
        find_sub(ch1[num])


for tc in range(1, int(input()) + 1):
    v, e, target_1, target_2 = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 1

    par = [0] * (v + 1)

    ch1 = [0] * (v + 1)
    ch2 = [0] * (v + 1)

    for i in range(0, e * 2, 2):
        v1, v2 = arr[i], arr[i + 1]

        par[v2] = v1

        if ch1[v1] == 0:
            ch1[v1] = v2
        else:
            ch2[v1] = v2

    node = find_node(target_1, target_2)

    find_sub(node)

    print(f'#{tc} {node} {answer}')
