import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_set(node):
    while node != parents[node]:
        node = parents[node]
    return node


n = int(input())
m = int(input())
parents = list(range(n + 1))
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 'YES'

for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            parents[col + 1] = parents[row + 1]

numbers = list(map(int, input().split()))

num = parents[numbers[0]]
for number in numbers:
    if parents[number] != num:
        answer = 'NO'

print(answer)
