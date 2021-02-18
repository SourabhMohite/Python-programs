"""Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7"""

def DigCount(num):
	count=0
	digit=0
	while num!=0:
		count=count+1
		num=num//10


	return count


def main():
	value=int(input("Enter the number:"))
	iRet=DigCount(value)
	print("Number of digits in {} is:{}".format(value,iRet))

if __name__=="__main__":
	main()
