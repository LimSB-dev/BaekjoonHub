input()
print(sum(all(i%j for j in range(2,i))*i>1 for i in map(int,input().split())))