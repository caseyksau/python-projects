import math

def sum(a,b):
	return a + b

def sub(a,b):
	return a - b

def mult(a,b):
	return a * b

def div(a,b):
	return a / b
	
def result(num1,oper,num2):

	if oper == '+':
		print(sum(num1,num2))
	elif oper == '-':
		print(sub(num1,num2))
	elif oper == '/':
		print(div(num1,num2))
	elif oper == '*':
		print(mult(num1,num2))
	else:
		print('this is invalid')

def init():
	print('This is my simple calculator')

	num1 = input('Enter first number: ')
	while not num1.isdigit():
		num1 = input('Must be a #, Enter first number: ')

	oper = input('Enter operator (+,-,*,/): ')
	while not oper == '+' or oper == '-' or oper == '*' or oper == '/':
		oper = input('invalid entry, must be an operator: ')

	num2 = input('Enter second number: ')
	while not num2.isdigit():
		num2 = input('Must be a #, Enter first number: ')

	result(int(num1), oper, int(num2))


init()

