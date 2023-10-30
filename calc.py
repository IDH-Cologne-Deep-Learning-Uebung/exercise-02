while True:
    print("Enter number 1: ")
    num1 = int(input())
    
    print("Enter number 2: ")
    num2 = int(input())
    
    print("Enter the math operation ('add'/'addition' or 'multi'/'multiplication'): ")
    math_operation = input()
    if math_operation == "addition" or math_operation == "add":
        result = num1+num2
        print("Sum: " + str(result))
    elif math_operation == "multiplication" or math_operation == "multi":
        result = num1*num2
        print("Product: " + str(result))
    else:
        print("You entered an invalid math operation.") 
        
    print("Do you want to continue? Enter 'yes' or 'no': ")
    continue_input = input() 
    if continue_input != "yes":
        break
    
