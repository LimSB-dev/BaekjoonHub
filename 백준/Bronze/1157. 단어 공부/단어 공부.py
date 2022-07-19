t = input().upper()
a = list(set(t))
b = []
for i in a:
  b.append(t.count(i))
if b.count(max(b))>1:
  print('?')
else:
  print(a[b.index(max(b))])