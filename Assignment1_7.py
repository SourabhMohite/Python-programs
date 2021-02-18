"""Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True """

def ChkDiv(num):
	if num%5==0:
		return True
	else:
		return False

def main():
	value=int(input("Enter the number:"))
	bRet=ChkDiv(value)

	if bRet==True:
		print("{} is Divisible by 5".format(value))
	else:
		print("{} is not Divisible by 5".format(value))

if __name__=="__main__":
	main()
