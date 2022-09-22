def pre_order(node):
    global pre_o

    if nodes[node] != '.':
        pre_o += nodes[node]
        pre_order(nodes.index(ch1[node]))
        pre_order(nodes.index(ch2[node]))


def in_order(node):
    global in_o

    if nodes[node] != '.':
        in_order(nodes.index(ch1[node]))
        in_o += nodes[node]
        in_order(nodes.index(ch2[node]))


def post_order(node):
    global post_o

    if nodes[node] != '.':
        post_order(nodes.index(ch1[node]))
        post_order(nodes.index(ch2[node]))
        post_o += nodes[node]


n = int(input())
nodes = ['.'] * (n + 1)
ch1 = ['.'] * (n + 1)
ch2 = ['.'] * (n + 1)
pre_o = ''
in_o = ''
post_o = ''

for i in range(1, n + 1):
    n, v1, v2 = map(str, input().split())

    nodes[i] = n

    ch1[i] = v1
    ch2[i] = v2

pre_order(1)
print(pre_o)
in_order(1)
print(in_o)
post_order(1)
print(post_o)