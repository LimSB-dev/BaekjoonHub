import sys

def isPrime(num):

	if num ==1:
		return False
	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			return False
	return True
		
		
while True:
	
	n = int(sys.stdin.readline())
	count = 0
	
	if n == 0:
		
		break
	

	else:
		
		for i in range(n+1,2*n+1):
			if isPrime(i):
				count += 1
				
	print(count)
