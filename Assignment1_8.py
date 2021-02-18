"""Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *"""

def Display(num):
	i=0
	for i in range(num):
		print("*",end=" ")

def main():
	value=int(input("Enter the number:"))
	Display(value)

if __name__=="__main__":
	main()