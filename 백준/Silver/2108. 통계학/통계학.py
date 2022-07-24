from collections import Counter
import sys

input = sys.stdin.readline
print = sys.stdout.write

def mean(list):
  return round(sum(list)/len(list))

def median(list):
  list.sort()
  mid = list[(len(list)-1)//2]
  return mid

def mode(list):
  mode_dict = Counter(list)
  modes = mode_dict.most_common()

  if len(list)> 1 :
    if modes[0][1] == modes[1][1]:
      M = modes[1][0]
    else:
      M = modes[0][0]
  else:
    M = modes[0][0]
  return M

def scope(list):
  return max(list) - min(list)

n = int(input())
li = []

for i in range(n):
  li.append(int(input()))

print(f'{mean(li)}\n')
print(f'{median(li)}\n')
print(f'{mode(li)}\n')
print(f'{scope(li)}\n')
