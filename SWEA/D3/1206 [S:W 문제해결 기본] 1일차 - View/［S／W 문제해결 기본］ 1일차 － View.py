t = 10
for tc in range(1,t+1):
  lenght = int(input())
  li = list(map(int, input().split()))
  result = 0
  for i in range(2, lenght - 2):
    if li[i] > li[i+1] and li[i] > li[i+2] and li[i] > li[i-1] and li[i] > li[i-2]:
      result += li[i] - max(li[i-2],li[i-1],li[i+1],li[i+2])
  print(f"#{tc} {result}")