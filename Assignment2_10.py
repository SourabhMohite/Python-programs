"""Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37 """

def Sumdigit(num):
	sum=0
	digit=0
	while num!=0:
		digit=num%10
		sum=sum+digit
		num=num//10
	return sum

def main():
	value=int(input("Enter the number:"))
	add=Sumdigit(value)
	print("Addition of digits is:",add)

if __name__=="__main__":
	main()

