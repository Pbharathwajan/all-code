x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = []

def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True

for i in x:
    if isPrime(i) is True:
        y.append(i)
    
print(y)

