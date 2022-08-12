import sys
sys.stdin = open('input.txt')

arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

words = input()

for i in arr:
  words = words.replace(i,'a')

print(len(words))