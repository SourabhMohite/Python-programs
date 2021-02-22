"""Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56 """

def Max(brr):
	max=0
	for i in range(len(brr)):
		if brr[i]>max:
			max=brr[i]
	return max

def main():
	no=0
	arr=[]
	num=int(input("Enter number of elements:"))
	for i in range(num):
		no=int(input())
		arr.append(no)
	iRet=Max(arr)
	print("Maximum is:",iRet)

if __name__=="__main__":
	main()

