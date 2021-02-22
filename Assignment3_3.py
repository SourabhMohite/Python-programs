"""Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5 """

def Min(brr):
	min=brr[0]
	for i in range(len(brr)):
		if brr[i]<min:
			min=brr[i]
	return min

def main():
	no=0
	arr=[]
	num=int(input("Enter number of elements:"))
	for i in range(num):
		no=int(input())
		arr.append(no)
	iRet=Min(arr)
	print("Minimum is:",iRet)

if __name__=="__main__":
	main()

