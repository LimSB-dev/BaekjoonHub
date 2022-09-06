t = int(input())
M = list(input())
A = 0
B = 0
for i in range(t):
	if M[i-1]=='A':
		A += 1
	else:
		B += 1
if A>B:
	print('A')
elif A==B:
	print('Tie')
else:
	print('B')
