case = 0
while True:
  l,p,v = map(int,input().split())
  case += 1

  if v == 0:
    break
  
  if v % p < l:
    print('Case %s: %d' %(case, (v//p)*l+v%p))
  
  else:
    print('Case %s: %d' %(case, (v//p)*l+l))