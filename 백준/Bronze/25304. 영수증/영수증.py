money = int(input())
n = int(input())
answer = 'No'
for i in range(n):
    price, cnt = map(int, input().split())
    money -= price * cnt

if money == 0:
    answer = 'Yes'

print(answer)
