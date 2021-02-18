"""Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120 """

def Fact(num):
	i=0
	fact=1
	while(num!=1):
		fact=fact*num
		num=num-1

	return fact

def main():
	value=int(input("Enter the number:"))
	iRet=Fact(value)
	print("Factorial of {} is:{}".format(value,iRet))

if __name__=="__main__":
	main()