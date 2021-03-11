num = int(input("Enter a number here: "))
numdupe = num
cube = 0

while numdupe > 0:
   cube += (numdupe % 10)**3
   numdupe = numdupe//10

if cube == num:
   print(f"The number {num} is an armstrong number.")
else:
   print(f"The number {num} is not an armstrong number.")

