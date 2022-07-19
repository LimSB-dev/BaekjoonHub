a = b = int(input())

loops=0

while True:
  loops+=1
  ten=a//10
  one=a%10
  c=ten+one
  a=int(str(a%10)+str(c%10))

  if (b==a):
    break
print(loops)