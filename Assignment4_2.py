"""Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18 """


multiplication=lambda num1,num2:num1*num2


def main():
	no=0
	no1=int(input("Enter First number:"))
	no2=int(input("Enter Second number:"))
	print(multiplication(no1,no2))

if __name__=="__main__":
	main()

