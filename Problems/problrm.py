num = 7

if num>1:
    for i in range (2,num):
        if num%i == 0:
            print(f'{num} is not prime')
            break
        elif num%i !=0:
            print(f'{num} is prime')
            break


