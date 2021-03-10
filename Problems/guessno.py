import random

print("Hello! In this program you will have to guess a randomly selected number between 0 and 20. ")

num_1 = random.randint(0,20)
runw = True


def gnum():
    while runw == True:
        usernum = input("Please enter your guess here: ")
        user_num = int(usernum)
        if user_num < num_1:
            print("The number you guessed was lower than the number. Guess again.")
            continue
        if user_num > num_1:
            print("The number you guessed was higher than the number. Guess again.")
            continue
        if user_num == num_1:
            print (f"Your Guess was correct! The number was {num_1}")
            break

gnum()






