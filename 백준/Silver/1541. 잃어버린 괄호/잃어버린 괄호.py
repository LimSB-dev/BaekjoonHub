li = input().split('-')

anw = 0

for i in li[0].split('+'):
  anw += int(i)

for i in li[1:]:
  for j in i.split('+'):
    anw -= int(j)
    
print(anw)