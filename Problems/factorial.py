x = int(input("Enter a number here: "))
fact = 1
for i in range (1, x+1):
    fact*=i

print(f"The factorial of {x} is {fact}!")