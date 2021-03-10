
terms = int(input("Enter number of terms: "))

n1, n2 = 0,1

count = 0

if terms < count:
    print("Enter a positive integer!")
    end()
elif terms == 1:
    print(n1)
else:
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1



    

