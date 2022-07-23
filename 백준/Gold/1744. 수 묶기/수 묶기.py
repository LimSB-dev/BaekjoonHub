n = int(input())
mi = []
anw = []
pl = []

for i in range(n):
  a = int(input())
  if a <= 0:
    mi.append(a)
  else:
    pl.append(a)

mi.sort()
pl.sort(reverse = True)

# 음수 및 0
for i in range((len(mi)+1)//2):
  if i == len(mi)//2 and len(mi) % 2 != 0:
    i *= 2
    anw.append(mi[i])

  else:
    i *= 2
    anw.append(mi[i]*mi[i+1])

# 양수
for i in range((len(pl)+1)//2):
  if i == len(pl)//2 and len(pl) % 2 != 0:
    i *= 2
    anw.append(pl[i])

  else:
    i *= 2
    if pl[i] == 1 or pl[i+1] == 1:
      anw.append(pl[i]+pl[i+1])

    else:
      anw.append(pl[i]*pl[i+1])

print(sum(anw))