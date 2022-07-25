import sys
input = sys.stdin.readline

n,m = map(int,input().split())
li = list(map(int,input().split()))
min_tree, max_tree = 1, max(li)

while min_tree <= max_tree:
  cut = (max_tree + min_tree) // 2
  total = 0

  total = sum(i - cut if i -cut > 0 else 0 for i in li)
  
  '''
  for i in li:
    if i > cut:
      total += i - cut
  '''

  if total >= m:
    min_tree = cut + 1
  
  elif total < m:
    max_tree = cut - 1

print(max_tree)