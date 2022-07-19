anw = 0

for i in range(8):
    li = input()
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if li[j] == 'F':
                    anw += 1
    if i % 2 != 0:
        for j in range(8):
            if j % 2 != 0:
                if li[j] == 'F':
                    anw += 1

print(anw)