while True:
  li = input()
  p = 0
  b = 0
  now = []
  ans = 0
  if len(li) == 1 and li == '.':
    break

  for i in range(len(li)):
    
    if li[i] == '(':
      p += 1
      now.append('P')

    elif li[i] == '[':
      b += 1
      now.append('B')

    elif li[i] == ')':
      p -= 1
      if p < 0 or b < 0:
        ans = 'no'
        print(ans)
        break
      if now.pop() == 'B':
        ans = 'no'
        print(ans)
        break
      

    elif li[i] == ']':
      b -= 1
      if p < 0 or b < 0:
        ans = 'no'
        print(ans)
        break
      if now.pop() == 'P':
        ans = 'no'
        print(ans)
        break

    else:
      pass
    
  if ans == 'no':
    pass

  elif len(now) != 0:
    ans = 'no'
    print(ans)
  
  else:  
    print('yes')