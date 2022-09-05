t = int(input())

for _ in range(t):
    li = list(map(str,input().strip()))
    cnt = 0

    if li.count('(') == li.count(')'):
        for i in range(len(li)):
            if li[i] == '(':
                cnt += 1
            elif li[i] == ')':
                cnt -= 1
            if cnt < 0:
                print('NO')
                break
            if i == len(li) - 1 and cnt == 0:
                print('YES')
    else:
        print('NO')
