import sys
import math
input = sys.stdin.readline

n,k = map(int,input().split())
a = math.factorial(n)
b = math.factorial(k)
c = math.factorial(n-k)

print(int(a/(b*c)))