x = int(input("Enter a number here: "))
num = x
revnum = 0


while num > 0:
    revnum = revnum*10 + num % 10
    num = num//10

print(revnum)