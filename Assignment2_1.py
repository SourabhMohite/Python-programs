"""Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user. """
from Arithmetic import *;

def main():
	num1=int(input("Enter First Number:"))
	num2=int(input("Enter Second Number:"))
	iRet1=Add(num1,num2)
	iRet2=Sub(num1,num2)
	iRet3=Mult(num1,num2)
	iRet4=Div(num1,num2)
	print("Addition of {} and {} is:{}".format(num1,num2,iRet1))
	print("Substraction of {} and {} is:{}".format(num1,num2,iRet2))
	print("Multiplication of {} and {} is:{}".format(num1,num2,iRet3))
	print("Division of {} and {} is:{}".format(num1,num2,iRet4))

if __name__=="__main__":
	main()
