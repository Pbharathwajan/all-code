num = int(input("Enter number:"))
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num = num // 2 

print(f"Number in binary is: {binary}")