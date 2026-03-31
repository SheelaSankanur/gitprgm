print("Simple calculator")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
while True:
    operation = int(input("Enter your choice (1-5): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operation==1:
        print("Result:", num1 + num2)
    elif operation==2:
        print("Result:", num1 - num2)
    elif operation==3:
        print("Result:", num1 * num2)
    elif operation==4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")  
    else:
        if operation==5:
            print("Exiting the calculator. Goodbye!")
            break
        else:            
            print("Invalid choice. Please select a valid operation (1-5).")    
            