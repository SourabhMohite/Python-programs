"""Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
 * * * *
 * * *
 * *
 * """

def Display(num):
 	i=0
 	j=0
 	num1=num
 	for i in range(num):
 		for j in range(num1):
 			print("*",end=" ")
 		num1=num1-1
 		print()

def main():
	value=int(input("Enter the number:"))
	Display(value)

if __name__=="__main__":
	main()