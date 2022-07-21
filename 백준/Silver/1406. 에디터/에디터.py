import sys
input = sys.stdin.readline
print = sys.stdout.write

li_f = list(input().strip())
li_b = []
n = int(input())

for i in range(n):
  A = input().strip()
  if A[0] == 'L':
    if li_f == []:
      continue
    else:
      li_b.append(li_f.pop())
  elif A[0] == 'D':
    if li_b == []:
      continue
    else:
      li_f.append(li_b.pop())
  elif A[0] == "B":
    if li_f == []:
      continue
    else:
      li_f.pop()
  elif A[0] == 'P':
    li_f.append(A[2])

print(''.join(li_f + list(reversed(li_b))))
