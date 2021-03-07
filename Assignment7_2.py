"""Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects. """

class BankAccount:
	ROI=10.5
	def __init__(self,name,amount=0):
		self.Name=name
		self.Amount=amount

	def Deposit(self):
		self.Amount=int(input("Enter the amount to deposit:"))

	def Withdraw(self):
		with_amount=int(input("Enter the amount to be Withdraw:"))
		if with_amount<=self.Amount:
			self.Amount=self.Amount-with_amount

	def CalculateIntrest(self):
		return self.Amount*BankAccount.ROI

	def Display(self):
		print("Name:",self.Name)
		print("Amount:",self.Amount)

def main():
	obj1=BankAccount("Ram")
	obj1.Deposit()
	obj1.Withdraw()
	print("Interest:",obj1.CalculateIntrest())
	obj1.Display()

	obj2=BankAccount("Sham")
	obj2.Deposit()
	obj2.Withdraw()
	print("Interest:",obj2.CalculateIntrest())
	obj2.Display()

	obj3=BankAccount("Ramesh")
	obj3.Deposit()
	obj3.Withdraw()
	print("Interest:",obj3.CalculateIntrest())
	obj3.Display()


if __name__=="__main__":
	main()