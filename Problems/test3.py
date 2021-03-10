n = input("Enter number here: ")
f = int(n)
y =[]


for i in range(3):
    x = int(str(n)[i])
    y.append(x)

c = int(y[0]**3 + y[1]**3 + y[2]**3)
print(c)

if c == f:
    print("The number", n, " is a narcissistic number")
else:
    print(f"The number {n} is not a narcissitic number")