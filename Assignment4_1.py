"""Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64 """

power=lambda num:pow(2,num)


def main():
	no=0
	no=int(input("Enter the number:"))
	print(power(no))

if __name__=="__main__":
	main()

