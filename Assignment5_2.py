"""Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5"""
no1=0
def DisplayR(no):
	global no1
	
	if no>no1:
		print(no1+1,end=" ")
		no1=no1+1
		DisplayR(no)

def main():
	num=int(input("Enter the number:"))
	DisplayR(num)


if __name__=="__main__":
	main()