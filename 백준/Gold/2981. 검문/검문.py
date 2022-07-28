from math import*;w=n=p=d=0;b=[];exec('q=int(input());w=w or q;n=gcd(n,q-w);'*int(input()))
while~d*~d<=n:d+=1;b+=(n%d<1)*[d,n//d]
print(*sorted({*b})[1:])