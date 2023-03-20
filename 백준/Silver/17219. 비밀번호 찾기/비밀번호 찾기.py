import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
siteSet = {}
answer = []

for _ in range(n):
    site, password = input().split()
    siteSet[site] = password

for _ in range(m):
    site = input().strip()
    password = siteSet[site]
    answer.append(password)

print(*answer, sep='\n')
