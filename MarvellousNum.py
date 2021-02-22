def ChkPrime(num):
	count=0
	for i in range(1,num,1):
		if num%i==0:
			count=count+1
			
	
	if count>1:
		return False
	else:
		return True
	count=0
