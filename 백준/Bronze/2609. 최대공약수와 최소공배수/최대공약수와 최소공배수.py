n, m = map(int, input().split())
a = 1

while True:
    if n % a == 0 and m % a ==0:
        A = a
    if a == m:
        break
    a += 1
print(f'{A}\n{n*m//A}')