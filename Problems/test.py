import math

x = int(input("Enter a number here: "))

ser = 0
j = 1

for i in range (1,x+1):
    j = j*i
    ser += (x**i)/j
    
ser = ser+1
print(ser)
