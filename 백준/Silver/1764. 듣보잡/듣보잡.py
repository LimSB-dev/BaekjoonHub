n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(input())
for _ in range(m):
    arr2.append(input())

arr1 = set(arr1)
arr2 = set(arr2)

answer = arr1 & arr2

answer = sorted(list(answer))

print(len(answer))
for i in answer:
    print(i)