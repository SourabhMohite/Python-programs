"""Write a program which display 10 to 1 on screen.
Output : 10 9 8 7 6 5 4 3 2 1"""

def Display(num):
	i=0
	for i in range(num,0,-1):
		print(i)

def main():
	value=int(input("Enter the number:"))
	Display(value) 

if __name__=="__main__":
	main()
