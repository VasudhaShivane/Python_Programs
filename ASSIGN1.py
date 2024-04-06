def calculator():
    print("Calculator")
    while True:

        print("\n")
        print(" '+' for ADDITION")
        print(" '-' for SUBTRACTION")
        print(" '*' for MULTIPLICATION")
        print(" '/' for DIVISION")
        print(" '^' for EXPONENTIAL'")
        print(" 'end' to end the program")
        print("\n")

        # Get user input
        user_input = input("Operation :  ")

        # Check if the user wants to quit
        if user_input == "end":
            break
        # Check if the user input is a valid operator
        elif user_input in ["+", "-", "*", "/"]:
            # Get first number
            num1 = float(input("Enter first number: "))
            # Get second number
            num2 = float(input("Enter another number: "))

            # Perform the operation based on the user input
            if user_input == "+":
                result = num1 + num2
                print("Addition : ", num1, "+", num2, "=", result)

            elif user_input == "-":
                result = num1 - num2
                print("Subtraction : ",num1, "-", num2, "=", result)

            elif user_input == "*":
                result = num1 * num2
                print("Multiplication : ",num1, "*", num2, "=", result)

            elif user_input == "/":
                result = num1 / num2
                print("Division : ",num1, "/", num2, "=", result)

            elif user_input == "^":
                result = num1 ^ num2
                print("Exponential : ",num1, "^", num2, "=", result)

        else:
            # In case of invalid input
            print("Invalid Input")
calculator()
