for t in range(int(input())):
    print(f'#{t+1} {"yes" if input().count("1")%2 else "no"}')