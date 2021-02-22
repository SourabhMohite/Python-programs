"""Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 256, 1024]
Output of reduce = 1320"""

import functools as fn

Check=lambda brr: brr%2==0
Increment=lambda crr:pow(2,crr)
Mul=lambda a,b:a+b

def main():
	no=0
	num=0
	rRet=0
	arr=[]
	fRet=[]
	mRet=[]
	no=int(input("Enter number of elements:"))
	print("Enter the Elements:")
	for i in range(no):
		num=int(input())
		arr.append(num)
	fRet=list(filter(Check,arr))
	print("List After Filter:",fRet)
	mRet=list(map(Increment,fRet))
	print("List After Map:",mRet)
	rRet=fn.reduce(Mul,mRet)
	print("Reduces output is:",rRet)
	


if __name__=="__main__":
	main()
