t = int(input())
for i in range(t):
    n = int(input())
    li = ""
    for _ in range(n):
        ci, ki = input().split()
        li += ci * int(ki)

    print(f"#{i+1}")

    for i in range(0, len(li), 10):
        print(li[i:i+10])