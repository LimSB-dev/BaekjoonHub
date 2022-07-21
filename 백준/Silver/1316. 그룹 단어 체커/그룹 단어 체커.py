t = int(input())
answer = 0
for _ in range(t):
  n = list(input())
  prev = n.pop(0)
  table = set(prev)
  is_group = True
  for word in n:
    if word in table:
      if word != prev: 
        is_group = False
        break
    table.add(word)
    prev = word
  if is_group:
    answer += 1
print(answer)