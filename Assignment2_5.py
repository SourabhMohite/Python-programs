"""Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number"""


def Chkprime(num):
	i=0
	j=0
	for i in range(1,num+1,1):
		if num%i==0:
			j=j+1
			if(j>2):
				break

	if(j>2):
		return False
	else:
		return True


def main():
	value=int(input("Enter the Number:"))
	bRet=Chkprime(value)
	if bRet==True:
		print("Number is prime")
	else:
		print("Number is not prime")


if __name__=="__main__":
	main()