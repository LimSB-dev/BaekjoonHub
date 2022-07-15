n = int(input())
li = list(map(int, input().split()))

li.sort()

print(li[(n - 1)// 2])