lim = int(input("Enter a number here: "))
x = 0
y = 1
z = 1
count = lim
while count > 0:
    x = y
    y = z
    z = x+y
    count -= 1

print(z)