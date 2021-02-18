"""Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero"""

def Chkposneg(num):
	if num<0:
	   return False
	else:
		return True

def main():
	value=int(input("Enter number to be check:"))
	bRet=Chkposneg(value) 

	if bRet==True:
		print("{} is Positive".format(value))
	else:
		print("{} is Negative".format(value))

if __name__=="__main__":
	main()