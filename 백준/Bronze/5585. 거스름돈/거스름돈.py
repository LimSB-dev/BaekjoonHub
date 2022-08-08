n = int(input())
pay_back = 1000 - n
li = [500,100,50,10,5,1]
cnt = 0
for i in range(len(li)):
  if pay_back >= li[i]:
    cnt += pay_back // li[i]
    pay_back = pay_back % li[i]

print(cnt)