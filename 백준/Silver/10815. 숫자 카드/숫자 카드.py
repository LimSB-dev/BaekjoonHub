n = int(input())
li_n = set(map(int,input().split()))
m = int(input())
li_m = list(map(int,input().split()))

for i in range(len(li_m)):
  if li_m[i] in li_n:
    print(1,end=' ')
  else:
    print(0,end=' ')