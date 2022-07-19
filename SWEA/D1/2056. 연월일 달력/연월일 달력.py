t = int(input())

for tc in range(1,t+1):
    li = input()
    year = li[:4]
    month = li[4:6]
    day = li[6:]
    
    if int(month) in [1,3,5,7,8,10,12]:
        if int(day) < 1 or 31 < int(day):
            print(f'#{tc} -1')
            
    if int(month) in [4,6,9,11]:
        if int(day) < 1 or 30 < int(day):
            print(f'#{tc} -1')
            
    if int(month) == 2:
        if int(day) < 1 or 28 < int(day):
            print(f'#{tc} -1')

    if int(month) < 1 or 12 < int(month):
        print(f'#{tc} -1')
    
    print(f'#{tc} {year}/{month}/{day}')