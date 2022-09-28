t = int(input())
A = 0
B = 0
for i in range(t):
	if int(input())==1:
		A += 1
	else:
		B += 1
if A>B:
	print('Junhee is cute!')
	
else:
	print('Junhee is not cute!')