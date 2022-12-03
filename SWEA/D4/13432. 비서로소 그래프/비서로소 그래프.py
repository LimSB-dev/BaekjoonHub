
T = int(input())
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x
def prime(n):
    if n%2 == 0: return 2
    p = 3
    while p*p<=n:
        if n%p ==0:
            return p
        else: p +=2
    return n
def bfs(n,s,t):
    g = gcd(s,t)
    if s==t:
        return 0
    elif s==1 or t==1:
        return -1
    elif g > 1:
        return 1
    p, q = prime(s), prime(t)
    if p*q <= n:
        return 2
    elif 2*p <= n and 2*q <= n:
        return 3
    else: return -1
 
 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, s,t = map(int,input().split())
    ans = bfs(n,s,t)
 
    print(f"#{test_case} {ans}")