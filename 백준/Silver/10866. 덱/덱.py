import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
li = []
for i in range(n):
    A = list(input().split())
    if A[0] == 'push_front':
        li.insert(0,int(A[1]))
    elif A[0] == 'push_back':
        li.append(int(A[1]))
    elif A[0] == 'pop_front':
        if sum(li) == 0:
            print('-1\n')
        else:
            print(f'{li.pop(0)}\n')
    elif A[0] == 'pop_back':
        if sum(li) == 0:
            print('-1\n')
        else:
            print(f'{li.pop(-1)}\n')
    elif A[0] == 'size':
        print(f'{len(li)}\n')
    elif A[0] == 'empty':
        if sum(li) == 0:
            print('1\n')
        else:
            print('0\n')
    elif A[0] == 'front':
        if sum(li) == 0:
            print('-1\n')
        else:
            print(f'{li[0]}\n')
    else:
        if sum(li) == 0:
            print('-1\n')
        else:
            print(f'{li[len(li) - 1]}\n')
