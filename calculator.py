def calculator():
    print("Welcome to the calculator!")
    
    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %, **): ")
        num2 = float(input("Enter the second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        elif operator == '**':
            result = num1 ** num2
        else:
            print("Invalid operator!")
            continue
        
        print("Result: ", result)
        
        choice = input("Do you want to perform another calculation? (yes/no): ")
        
        if choice.lower() != "yes":
            break

calculator()
