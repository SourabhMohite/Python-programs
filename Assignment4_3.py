"""Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000 """
import functools as fn
Check=lambda brr: brr>=70 and brr<=90
Increment=lambda crr:crr+10
Mul=lambda a,b:a*b

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
	fRet=filter(Check,arr)
	print("List After Filter:",fRet)
	mRet=map(Increment,fRet)
	print("List After Map:",mRet)
	rRet=fn.reduce(Mul,mRet)
	print("Reduces output is:",rRet)
	


if __name__=="__main__":
	main()
