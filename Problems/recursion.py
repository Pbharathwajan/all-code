def fact(n):
    if n==1:
      return 1 # 1! = 1
    else:
      # n! = (n-1)! * n
      return ( fact(n-1) * n )

def fibonacci(n):
    if n <=1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

for i in range (6):
    print(fibonacci(i))
