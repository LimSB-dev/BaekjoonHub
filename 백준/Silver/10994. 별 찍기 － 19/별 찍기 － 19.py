n = int(input())
a = 4 * n - 3
stars = [[' ' for _ in range(a)] for _ in range(a)]

def fill_stars(n, x, y):
  if n == 1:
    stars[y][x] = '*'
    return
  
  a = 4 * n - 3

  for i in range(a):
    stars[y][x + i] = '*'
    stars[y + i][x] = '*'
    stars[y + a - 1][x + i] = '*'
    stars[y + i][x + a - 1] = '*'

  fill_stars(n - 1, x + 2, y + 2)


fill_stars(n, 0, 0)

for s in stars:
  print(''.join(s))