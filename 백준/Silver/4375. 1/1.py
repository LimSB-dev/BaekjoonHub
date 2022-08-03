while True:
  try:
    n = int(input())
    num_1 = 1
    cnt = 1
  
    while num_1 % n != 0:
     num_1 += 10**cnt
     cnt += 1
    print(cnt)
  
  except:
    break