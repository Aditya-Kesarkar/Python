num1 = int(input("Enter num1  :")) 
num2 = int(input("Enter num2  :")) 
choice = input("Enter the your choice:\n Add(1)\t Sub(2)\t Mul(3)\t Div(4)\t Power(5)\n Floor Division(6)\t Remainder(7)\n ")

if (choice == "1"):
    print(f"The addition of {num1} & {num2} is: {num1+num2}")
elif(choice == "2"):
    print(f"The subtraction of {num1} & {num2} is: {num1-num2}")
elif (choice == "3"):
    print(f"The product of {num1} & {num2} is: {num1*num2}")
elif (choice == "4"):
    print(f"The division of {num1} & {num2} is: {num1/num2}")
elif (choice == "5"):
    pow = int(input("Enter the power to be checked: "))
    print(f"The result after power of {num1} & {num2} is: {num1 ** pow, num2 ** pow}")
elif (choice == "6"):
    print(f"The Floor division of {num1} & {num2} is: {num1//num2}")
elif (choice == "7"):
    print(f"The remainder(Modulo) of {num1} & {num2} is: {num1%num2}")
else:
    print("Invalid Choice!")  

