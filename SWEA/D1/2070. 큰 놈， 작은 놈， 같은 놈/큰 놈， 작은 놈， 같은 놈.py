for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    if a > b:
        print('>')
    elif a == b:
        print('=')
    else:
        print('<')