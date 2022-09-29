import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_set(node):
    if node != parents[node]:
        parents[node] = find_set(parents[node])
    return parents[node]


n = int(input())
m = int(input())
parents = list(range(n + 1))
answer = 'YES'

for row in range(n):
    arr = list(map(int, input().split()))
    for col in range(n):
        if arr[col] == 1:
            v1_root, v2_root = find_set(row + 1), find_set(col + 1)

            if v1_root != v2_root:
                if v1_root < v2_root:
                    parents[v2_root] = v1_root
                else:
                    parents[v1_root] = v2_root

numbers = list(map(int, input().split()))

num = parents[numbers[0]]
for number in numbers:
    if parents[number] != num:
        answer = 'NO'

print(answer)
