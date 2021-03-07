"""Write a program which contains one class named as Arithmetic.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects."""

class Arithmetic:
	Value=0
	def __init__(self,num):
		self.Number=num

	def ChkPrime(self):
		flag=False
		for i in range(2,int(self.Number/2)+1):
			if self.Number%i==0:
				flag=True
				break
		return flag

	def ChkPerfect(self):
		sum=0
		for i in range(1,int(self.Number/2+1)):
			if self.Number%i==0:
				sum=sum+i
		if sum==self.Number:
			return True
		else:
			return False


	def Factors(self):
		arr=[]
		for i in range(1,int(self.Number/2+1)):
			if self.Number%i==0:
				arr.append(i)
		return arr
		

	def SumFactors(self):
		sum=0
		for i in Arithmetic.Factors(self):
			sum=sum+i
		return sum

def main():
	num=int(input("Enter number:"))
	obj1=Arithmetic(num)
	if obj1.ChkPrime():
		print("Number is not prime")
	else:
		print("Number is prime")

	if obj1.ChkPerfect():
		print("Number is perfect")
	else:
		print("Number is not perfect")

	print("Factors are:")
	for i in obj1.Factors():
		print(i)

	print("Sum of Factors is:",obj1.SumFactors())




	num=int(input("Enter number:"))
	obj2=Arithmetic(num)
	if obj2.ChkPrime():
		print("Number is not prime")
	else:
		print("Number is prime")

	if obj2.ChkPerfect():
		print("Number is perfect")
	else:
		print("Number is not perfect")

	print("Factors are:")
	for i in obj2.Factors():
		print(i)

	print("Sum of Factors is:",obj2.SumFactors())

if __name__=="__main__":
	main()