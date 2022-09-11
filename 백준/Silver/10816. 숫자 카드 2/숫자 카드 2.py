from collections import Counter
m = int(input())
li_m = list(map(int,input().split()))
n = int(input())
li_n= list(map(int,input().split()))
cnt = Counter(li_m)

for i in li_n:
  print(cnt[i], end=' ')