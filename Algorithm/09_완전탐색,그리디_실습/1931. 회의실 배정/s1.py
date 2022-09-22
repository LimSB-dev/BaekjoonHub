import sys
sys.stdin = open('input.txt', encoding='utf-8')

n = int(input())
arr = []

for i in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

end = 0
count = 0

for i in arr:
    if i[0] >= end:
        end = i[1]
        count += 1

print(count)