import sys

c = 1

while True:

  a =int(sys.stdin.readline())

  n1 = 3 * a

  if a == 0 :

    break

  elif n1 % 2 ==0:

    n2 = n1 / 2

    n3 = 3 * n2

    n4 = n3 // 9

    print (f'{c}.','even',int(n4))

    c += 1

  else:

    n2 = (n1+1)/2

    n3 = 3 * n2

    n4 = n3 // 9

    print (f'{c}.','odd',int(n4))

    c += 1