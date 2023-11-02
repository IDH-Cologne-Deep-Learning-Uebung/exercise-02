def calculate():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter operator(add for addition; mult for multiplication):")
    operator = str(input())
    if operator == "add" or "+":
        print("Sum: " + str(num1+num2))
    if operator == "mult" or "*":
        print("Product: " + str(num1*num2))
        
x = 0

calculate()

while x < 1:
    print("Do you want to continue? (y/n)")
    answer = str(input())
    if answer == "y":
        calculate() 
    if answer == "n":
        x = 1