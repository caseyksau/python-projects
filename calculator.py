mem = [] # trying to limit list to a set length

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
		print(num1, oper, num2, '=', sum(num1,num2),'\n\n')
		mem.insert(0,sum(num1,num2))
	elif oper == '-':
		print(num1, oper, num2, '=', sub(num1,num2),'\n\n')
		mem.insert(0,sub(num1,num2))
	elif oper == '/':
		print(num1, oper, num2, '=', div(num1,num2),'\n\n')
		mem.insert(0,div(num1,num2))
	elif oper == '*':
		print(num1, oper, num2, '=', mult(num1,num2),'\n\n')
		mem.insert(0,mult(num1,num2))
	else:
		print('this is invalid')

def init():
	print("This is my simple calculator, to exit, press 'ctrl + d'")

	# getting FIRST #
	if len(mem) == 0:
		num1 = input('Enter first number:\n')
	else:
		# print array memory
		print('Memory: ',mem)
		num1 = input("Enter number or \npress 'r' for last result\n")
	while not num1.isdigit():
		if num1 == 'r':
			num1 = mem[0]
			print(num1)
			break
		if len(mem) == 0:
			num1 = input('Must be a #, Enter first number:\n')
		else:
			num1 = input("Must be a #, Enter first number or press 'r' for last result\n")

	# getting OPERATOR
	oper = input('Enter operator (+,-,*,/):\n')
	while oper not in ('+','-','*','/'):
		oper = input('invalid entry, must be an operator:\n')

	# getting SECOND #
	num2 = input('Enter second number:\n')
	while not num2.isdigit():
		num2 = input('Must be a #, Enter second number:\n')

	# returning results
	result(int(num1), oper, int(num2))

	# re-running calculator
	init()


init()

