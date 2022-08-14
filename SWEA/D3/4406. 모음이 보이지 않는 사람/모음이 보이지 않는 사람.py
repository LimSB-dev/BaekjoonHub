vowels = ['a', 'e', 'i', 'o','u']

for tc in range(1, int(input()) + 1):
    words = input()
    for i in vowels:
        words = words.replace(i, '')
    print(f'#{tc} {words}')
