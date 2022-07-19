import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
words = [input() for _ in range(n)]

words.sort(key = lambda x: (len(x),x))

prev = ''
for x in words:
  if x != prev:
    print(x)
  prev = x