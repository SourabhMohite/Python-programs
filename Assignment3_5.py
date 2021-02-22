"""Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)"""

from MarvellousNum import ChkPrime

def ListPrime(brr):
	sum=0
	for i in range(len(brr)):
		if ChkPrime(brr[i]):
			sum=sum+brr[i]
	return sum

def main():
	no=0
	arr=[]
	num=int(input("Enter number of elements:"))
	for i in range(num):
		no=int(input())
		arr.append(no)
	iRet=ListPrime(arr)
	print("Addtion of prime numbers is: ",iRet)

if __name__=="__main__":
	main()

