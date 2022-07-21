s = list(map(int,input().rstrip()))
cnt = 0

for i in range(1,len(s)):
  if s[i] != s[i-1]:
    cnt += 1

if cnt == 0:
  print(0)

else:
  print((cnt+1)//2)