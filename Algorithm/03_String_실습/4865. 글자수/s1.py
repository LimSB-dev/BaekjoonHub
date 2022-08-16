import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 0
    str1 = set(input().strip())
    str2 = input()
    cnt = 0
    
    for i in str1:
        cnt = str2.count(i)
        
        if answer < cnt:
            answer = cnt
    
    print(f'#{tc} {answer}')
