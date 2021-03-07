"""Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects."""


class Arithmetic:
	
	def __init__(self):
		self.Value1=0
		self.Value2=0
		
	def Accept(self):
		self.value1=int(input("Enter the value1:"))
		self.value2=int(input("Enter the value2:"))

	def Addition(self):
		return self.value1+self.value2

	def Substraction(self):
		return self.value1-self.value2

	def Multiplication(self):
		return self.value1*self.value2

	def Division(self):
		return self.value1/self.value2

def main():
	obj1=Arithmetic()
	obj1.Accept()
	print("Addition is:",obj1.Addition())
	print("Substraction is:",obj1.Substraction())
	print("Multiplication is:",obj1.Multiplication())
	print("Division is:",obj1.Division())

	obj2=Arithmetic()
	obj2.Accept()
	print("Addition is:",obj2.Addition())
	print("Substraction is:",obj2.Substraction())
	print("Multiplication is:",obj2.Multiplication())
	print("Division is:",obj2.Division())

	obj3=Arithmetic()
	obj3.Accept()
	print("Addition is:",obj3.Addition())
	print("Substraction is:",obj3.Substraction())
	print("Multiplication is:",obj3.Multiplication())
	print("Division is:",obj3.Division())
	
if __name__=="__main__":
	main()

