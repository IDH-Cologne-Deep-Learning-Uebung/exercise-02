def main(): 
  print("Enter 'add' to sum two numbers. Enter 'multi' to multiply two numbers. ")
  op = str(input())
  print("Enter number 1: ")
  num1 = int(input())
  print("Enter number 2: ")
  num2 = int(input())
  if (op == "add"):
    print("Sum: " + str(num1+num2)) 
  if (op == "multi"): 
    print("Product: " + str(num1*num2))
  return

rr = "y"
while rr == "y":
    main()
    print("Do you want to calculate again? (y/n) ")
    rr = str(input())