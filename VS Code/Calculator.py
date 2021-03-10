x = int(input("Enter first number here: "))
y = int(input("Enter second number here: "))

operation = input("Enter operation(Add,Subtract,Divide,Multiply): ")

if operation == "Add" :
    z = x + y
    print(f"The sum of the numbers is: {z} ")

elif operation == "Multiply":
    z = x * y
    print(f"The product of the numbers is: {z}")

elif operation == "Divide":
    z = x // y
    print(f"The dividend of the numbers is: {z} ")
    
elif operation == "Subtract":
    z = x - y
    print(f"The remainder of the numbers is: {z}")
    