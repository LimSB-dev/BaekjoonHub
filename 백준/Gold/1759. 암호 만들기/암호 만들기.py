from itertools import combinations

l, c = map(int,input().split())
li = input().split()
li.sort()
vowel = {'a', 'e', 'i', 'o', 'u'} # 모음
consonant = set(list('abcdefghijklmnopqrstuvwxyz')) - vowel

candidate = combinations(range(len(li)),l)

for value in candidate:
  anw = []
  for i in range(l):
    anw.append(li[value[i]])
  if len(set(anw) & vowel) >= 1 and len(set(anw) & consonant) >= 2:
    print(*anw,sep='')