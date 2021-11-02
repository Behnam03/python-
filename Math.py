while True:
	print("Options")
	print("Taschenrechner")	
	print("Enter 'add' to add two Nambers")
	print("Enter 'subtract' to add two Nambers")
	print("Enter 'mltiplay' to add two Nambers")
	print("Enter 'divide' to add two Nambers")
	print("Enter 'quit' to end the program")
	user_input = input(":  ")
	if user_input == "quit":
		print("exsit")
		break
	elif 	user_input == "add":
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the secound number: "))
		result = str(num1 + num2)
		print("The answer: "+ result)
	elif 	user_input == "subtract":
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the secound number: "))
		result = str(num1 -num2)
		print("The answer: "- result)
	elif 	user_input == "multiply":
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the secound number: "))
		result = str(num1 * num2)
		print("The answer: "* result)
	elif 	user_input == "divide":
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the secound number: "))			
		result = str(num1 / num2)
		print("The answer: "/ result)
