input_data = input().split(' ')
H = int(input_data[0])
M = int(input_data[1])

if M<45:
  if H==0 :
    print((H+23), (M+15))
  else:
    print((H-1), (M+15))
else:
   print((H), (M-45))