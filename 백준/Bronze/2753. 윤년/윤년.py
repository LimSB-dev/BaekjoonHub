yyyy = int(input())
if yyyy%400==0:
  print('1')
elif yyyy%100==0:
  print('0')
elif yyyy%4==0:
  print('1')
else:
  print('0')