import sys

n = int(sys.stdin.readline())
N = []

for i in range(n):

  N.append(int(sys.stdin.readline()))

N.sort()

for i in range(len(N)):

  print(N[i])