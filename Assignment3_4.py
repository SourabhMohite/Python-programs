"""Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3 """

def Frequency(brr,num1):
	freq=0
	for i in range(len(brr)):
		if brr[i]==num1:
			freq=freq+1
	return freq

def main():
	no=0
	arr=[]
	num=int(input("Enter number of elements:"))
	for i in range(num):
		no=int(input())
		arr.append(no)
	value=int(input("Enter element to search:"))
	iRet=Frequency(arr,value)
	print("Frequency of {} is:{}:".format(value,iRet))

if __name__=="__main__":
	main()

