from itertools import combinations

li = []

for _ in range(9):
    n = int(input())
    li.append(n)

for i in combinations(li, 7):
    if sum(i) == 100:
        anw = list(i)
        break

anw.sort()

for i in anw:
    print(i)
