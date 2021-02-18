"""Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20 """

def Display():
	j=0
	i=0
	for i in range(2,100,2):
		print(i)
		j=j+1
		if j==10:
			break


def main():
	Display()

if __name__=="__main__":
	main()