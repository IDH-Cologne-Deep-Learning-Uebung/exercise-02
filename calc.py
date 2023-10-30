conti = "y"
while conti=="y":

    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print("Enter operation: ")
    operation = str(input())


    if operation == "add" :
        print("Sum: " + str(num1+num2))

    if operation == "addition" :
        print("Sum: " + str(num1+num2))


    if operation == "multi" :
        print("Product: " + str(num1*num2))

    if operation == "multiplication" :
        print("Product: " + str(num1*num2))


    print("Continue? [y/n]: ")
    conti = str(input())
    if conti == "y":
        print()
