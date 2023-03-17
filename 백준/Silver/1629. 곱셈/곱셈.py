a, b, c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a**2) % c    
    else:
        if b % 2:
            return ((solution(a,b//2,c)**2) * a) % c
        else:
            return ((solution(a,b//2,c)**2)) % c
        
print(solution(a, b, c))