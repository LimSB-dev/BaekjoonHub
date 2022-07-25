import sys
input = sys.stdin.readline

n,m = map(int,input().split())

card = list(map(int,input().split()))
l = len(card)
anw = 0

for i in range(l):
  for j in range(l):
    if i == j:
      continue
    for k in range(l):
      if k == i or k == j:
        continue
      sum = card[i] + card[j] + card[k]
      if sum > m:
        continue
      elif sum > anw:
        anw = sum
print(anw)