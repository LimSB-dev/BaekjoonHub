import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
nums = [int(input()) for i in range(n)]

nums.sort(reverse=False)
for num in nums:
  print(f'%s\n'%num)