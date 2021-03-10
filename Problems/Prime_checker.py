
x = int(input("Enter number here: "))

for i in range(2,x):
    if x % i == 0:
        y = x/i
        print(f"The number {x} is not prime.")
        print(f"It is the product of {y} and {i}")
        break
    elif x % i != 0:
        print(f"{x} is a prime number.")
        if 
        break