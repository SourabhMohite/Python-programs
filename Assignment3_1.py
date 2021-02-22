"""Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130 """

def Addition(brr):
	sum=0
	for i in range(len(brr)):
		sum=sum+brr[i]
	return sum

def main():
	no=0
	arr=[]
	num=int(input("Enter number of elements:"))
	for i in range(num):
		no=int(input())
		arr.append(no)
	iRet=Addition(arr)
	print("Addition is:",iRet)

if __name__=="__main__":
	main()

