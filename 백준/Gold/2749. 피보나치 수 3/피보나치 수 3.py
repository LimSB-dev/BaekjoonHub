M,n,a,b=int(1e6),int(input()),0,1
for i in range(63):
 a,b=(a*a+2*a*b)%M,(a*a+b*b)%M
 if n&(1<<(62-i))!=0:a,b=(a+b)%M,a
print(a)