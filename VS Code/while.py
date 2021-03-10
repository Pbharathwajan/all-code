import math
x = int(input("Enter upper limit here: "))
k = set(x)

for i in range (x-1):
    if {j for j in range(k)} % i == 0:
        print(f"The number {i} is not prime.")
    else:
        print(f"The number {i} is prime")
    