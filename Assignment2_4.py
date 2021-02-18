"""Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)"""

def AddFact(num):
    i=0
    sum=0
    #num1=num/2
    for i in range(1,num,1):
    	if num%int(i)==0:
    	   sum=sum+i
    return sum 

def main():
	value=int(input("Enter the number:"))
	iRet=AddFact(value)
	print("Addition of Factors of {} is:{}".format(value,iRet))

if __name__=="__main__":
	main()