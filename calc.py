print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
print("Enter operation: ")
op = str(input())
if op == "add" or op == "+":
    print("Sum: " + str(num1+num2))
if op == "multi" or op == "*":
    print("Product: " + str(num1*num2))
print("If you would like to continue, please enter the letter y. If not, n. ")
c = str(input())
while (c == "y"):
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter operation: ")
    op = str(input())
    if op == "add" or op == "+":
        print("Sum: " + str(num1+num2))
    if op == "multi" or op == "/":
        print("Product: " + str(num1*num2))
    print("If you would like to continue, please enter the letter y. If not, n. ")
    c = str(input())
        