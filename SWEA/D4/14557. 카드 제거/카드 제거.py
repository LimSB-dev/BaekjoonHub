for t in range(1, int(input()) + 1):
    print(f'#{t} {"yes" if input().count("1") % 2 == 1 else "no"}')