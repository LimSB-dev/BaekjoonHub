import sys
t = int(sys.stdin.readline())
if t % 10 != 0:
  print(-1)
else:
  a=b=c=0
  a=t//300
  b=t%300//60
  c=t%300%60//10
  print(a,b,c)