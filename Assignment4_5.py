"""Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62 """


import functools as fn

def Check(num):
	count=0
	for i in range(1,num,1):
		if num%i==0:
			count=count+1
	if count>1:
		return False
	else:
		return True
	count=0

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
	mRet=list(map(lambda a:a*2,fRet))
	print("List After Map:",mRet)
	rRet=fn.reduce(lambda a,b:a if a>b else b,mRet)
	print("Reduces output is:",rRet)
	
if __name__=="__main__":
	main()

