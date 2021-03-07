"""Write a recursive program which accept number from user and return its
factorial.
Input : 5

Output : 120 """


def FactR(no):
	if no==0:
		return 1
	return no*FactR(no-1)

def main():
	num=int(input("Enter the number:"))
	iRet=FactR(num)
	print("Summation is:",iRet)


if __name__=="__main__":
	main()