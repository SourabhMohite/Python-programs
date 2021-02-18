"""Write a program which display 5 times Marvellous on screen.
Output : Marvellous
 Marvellous
 Marvellous
 Marvellous
 Marvellous"""

def Display(num):
 	i=0
 	for i in range(num):
 		print("Marvellous")

def main():
 	value=int(input("Enter the number:"))
 	Display(value)

if __name__=="__main__":
	main()
