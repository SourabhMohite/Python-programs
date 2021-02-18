""" Write a program which accept one number and display below pattern.
Input : 5
Output :
 * * * * *
 * * * * *
 * * * * *
 * * * * *
 * * * * * """
def Display(num):
 	i=0
 	j=0
 	for i in range(num):
 		for j in range(num):
 			print("*" ,end=" ")

 		print()


def main():
 	value=int(input("Enter the number:"))
 	Display(value)

if __name__=="__main__":
	main()


