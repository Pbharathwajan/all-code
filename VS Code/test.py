import math


x = int(input("Enter a number here: "))


ser = 0
v = 1

for i in range (x):
    j = math.factorial(i)
    ser += (x**i)/j
    print(ser)
    
ser1 = ser+1
print(ser1)
