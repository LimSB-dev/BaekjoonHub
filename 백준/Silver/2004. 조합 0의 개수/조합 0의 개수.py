import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())

def cnt_2(num):
  cnt = 0
  while num != 0:
    num //= 2
    cnt += num
  return cnt

def cnt_5(num):
  cnt = 0
  while num != 0:
    num //= 5
    cnt += num
  return cnt

print(min(cnt_2(n) - cnt_2(n - m) - cnt_2(m), cnt_5(n) - cnt_5(n - m) - cnt_5(m)
))