import sys
sys.stdin = open('input.txt', encoding='utf-8')


def pre_order(node):
    global pre_list
    if node != 0:
        pre_list.append(node)
        pre_order(ch1[node])
        pre_order(ch2[node])


def in_order(node):
    global in_list
    if node != 0:
        in_order(ch1[node])
        in_list.append(node)
        in_order(ch2[node])


def post_order(node):
    global post_list
    if node != 0:
        post_order(ch1[node])
        post_order(ch2[node])
        post_list.append(node)


v, e = map(int, input().split())
arr = list(map(int, input().split()))

pre_list = []
in_list = []
post_list = []

ch1 = [0] * (v + 1)
ch2 = [0] * (v + 1)

for i in range(0, e):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]

    if ch1[v1] == 0:
        ch1[v1] = v2

    elif ch2[v1] == 0:
        ch2[v1] = v2

pre_order(1)
in_order(1)
post_order(1)

print('전위 순회 :', *pre_list)
print('중위 순회 :', *in_list)
print('후위 순회 :', *post_list)
