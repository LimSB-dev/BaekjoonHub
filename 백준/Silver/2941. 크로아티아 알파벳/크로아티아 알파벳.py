A = 'c=','c-','dz=','d-','lj','nj','s=','z='

L = input()

for i in A:
  
  L = L.replace(i,'^')

print(len(L))