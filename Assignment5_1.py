"""Write a recursive program which display below pattern.
Input : 5
Output : * * * * *"""

def DisplayR(no):
	if no!=0:
		print("*",end=" ")
		no=no-1
		DisplayR(no)

def main():
	num=int(input("Enter the number:"))
	DisplayR(num)


if __name__=="__main__":
	main()