C=int(input())
while C>0:
  over = 0
  S=list(map(int,input().split()))
  Av = (sum(S)-S[0])/S[0]
  for i in S[1:]:
    if i > Av:
      over += 1
  print(f'{over/S[0]*100:.3f}%')
  C -=1