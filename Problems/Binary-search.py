a = 1
b = int(input("Enter upper limit here: "))
guess = 23343


num = int(input("Enter number here: "))


if num < 1 and 100 < num:
    print ("Number must be between 1 and 100!")
    print("Run the code again.")
    exit()


while guess != num:
        guess = (a+b)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            b = guess
        elif guess < num:
            a = guess + 1
        if  guess == num:
            print (f'The computer took a guess and it was {num}!')