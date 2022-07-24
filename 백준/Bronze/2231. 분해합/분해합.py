n,o=int(input()),0
for i in range(n,1,-1):
    if sum(map(int,str(i)))+i==n:o=i
print(o)