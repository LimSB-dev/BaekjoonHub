import sys
#sys.stdin = open('input.txt')
from math import ceil,log2

input = sys.stdin.readline
p = 2000000

def update(b):
    while b>=1:
        tree[b]+=1
        b//=2

def rm_update(node,b):
    while node<size:
        if tree[node*2]<b:
            b-=tree[node*2]
            node=node*2+1
        else:
            node=node*2
    return node

size = 2**ceil(log2(p))
tree=[0]*(2*size)

n=int(input())

for i in range(n):
    t, x = map(int, input().split())
    if t == 1:
        update(size + x - 1)
    else:
        temp = rm_update(1, x)
        print(temp - size + 1)
        while temp >= 1:
            tree[temp] -= 1
            temp //= 2