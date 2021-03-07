"""Write a recursive program which accept number from user and return
summation of its digits.
Input : 879
Output : 24 """

sum=0
def SumR(no):
	global sum
	if no!=0:
		digit=no%10
		sum=sum+digit
		no=no//10
		SumR(no)
	return sum

def main():
	num=int(input("Enter the number:"))
	iRet=SumR(num)
	print("Summation is:",iRet)


if __name__=="__main__":
	main()