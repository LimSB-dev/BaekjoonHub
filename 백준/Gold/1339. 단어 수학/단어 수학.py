n = int(input())
alpha =[]
anw = 0

for _ in range(26):
  alpha.append(0)

for _ in range(n):
  word = input()
  for i in range(len(word)):
    alpha[ord(word[i]) - ord('A')] += 10**(len(word)- i - 1)

alpha.sort(reverse = True)

for i in range(26):
  if alpha[i] != 0:
    anw += alpha[i] * (9-i)
  else:
    break

print(anw)