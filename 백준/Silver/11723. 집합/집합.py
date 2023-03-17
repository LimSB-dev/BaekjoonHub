import sys
input = sys.stdin.readline

x_list = [False for _ in range(21)]

for _ in range(int(input())):
    operate = input().rstrip().split()
    cmd = operate[0]
    
    if cmd == 'add':
        idx = int(operate[1])
        x_list[idx] = True
    elif cmd == 'remove':
        idx = int(operate[1])
        x_list[idx] = False        
    elif cmd == 'check':
        idx = int(operate[1])
        print(1 if x_list[idx] else 0)
    elif cmd == 'toggle':
        idx = int(operate[1])
        x_list[idx] = not x_list[idx]
    elif cmd == 'all':
        for idx in range(21):
            x_list[idx] = True
    elif cmd == 'empty':
        for idx in range(21):
            x_list[idx] = False