#!/usr/bin/python3

# Addition of 2 values

class Calculator:
	"""docstring for Calculator"""
	def __init__(self, arg):
		super(Calculator, self).__init__()
		self.arg = arg
		

	def add(x, y):
		return x + y

	# Subtraction of 2 values

	def subtract(x, y):
		return x - y

	# Multiply 2 values

	def multiply(x, y):
		return x * y


	# Divide 2 values

	def divide(x, y):
		return x / y

	# Input from user

	print("Select any operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")

	while True:
		Choice = input("Enter Choice(1/2/3/4): ")

		if Choice in ('1', '2', '3', '4'): 

			namba1 = int(input("Enter 1st number: "))
			namba2 = int(input("Enter 2nd number: "))



			if Choice == '1':
				print(namba1, "+", namba2, "=", add(namba1,namba2))

			elif Choice == '2':
				print(namba1, "-", namba2, "=", subtract(namba1,namba2))

			elif Choice == '3':
				print(namba1, "*", namba2, "=", multiply(namba1,namba2))

			elif Choice == '4':
				print(namba1, "/", namba2, "=", divide(namba1,namba2))
			break

		else:
			print("Invalid input or few arguments, try again...")

