t = int(input())

for tc in range(1, t+1):

    n, m = map(int, input().split())
    li = [list(map(str, input().strip())) for _ in range(n)]

    even_set = ''
    odd_set = ''

    answer = 'possible'

    for row in range(n):
        for col in range(m):
            if li[row][col] != '?':
                if (row + col) % 2 == 0:
                    if even_set != '' and even_set != li[row][col]:
                        answer = 'impossible'
                    even_set = li[row][col]
                elif (row + col) % 2 == 1:
                    if odd_set != '' and odd_set != li[row][col]:
                        answer = 'impossible'
                    odd_set = li[row][col]

                if even_set == odd_set:
                    answer = 'impossible'
    print(f'#{tc} {answer}')
