import sys
input=sys.stdin.readline

Number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

li = list(input())

result = 0

for i in li :
  for j in Number :
    if i in j :
      result += Number.index(j) + 3
print(result)