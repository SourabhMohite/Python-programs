"""Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16 """


def Add(no1,no2):
	sum=no1+no2
	return sum

def main():
	num1=int(input("Enter First Number:"))
	num2=int(input("Enter Second Number:"))
	iRet=Add(num1,num2)
	print("Addition of {} and {} is {}".format(num1,num2,iRet))

if __name__=="__main__":
	main()


