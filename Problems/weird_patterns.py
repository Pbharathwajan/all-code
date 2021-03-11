def half_diamond(n):

    print('*')

    for i in range (1,n+1):
        print('*', end = "")

        for j in range (1,i+1):
            print(j,end= "")

        for j in range(i-1,0,-1):
            print(j,end = "")
        print('*',end="")
        print()

    for i in range (n-1,0,-1):
        print('*', end = "")
        for j in range (1,i+1):
            print(j, end = "")
        for j in range (i-1,0,-1):
            print(j, end = "")
        print('*',end = "")
        print()
    print('*')

def num_pyr(n):
    for i in range (n):
        for j in range (1,i+2):
            print(j, end = " ")
        print()


def back_num_pyr(n):
    k = 2*n - 2
    for i in range(n):
        for j in range (k):
            print(end = " ")
        k -=2

        for j in range(0,i+1):
            print(j, end = " ")
        print()

def back_star_pyr(n):
    k = 2*n - 2

    for i in range (0,n):
        for j in range (0,k):
            print(end = " ")
        k = k-2
    
        for j in range (0,i+1):
            print('*', end = " ")
        print("")


def star_pyr(n):
    for i in range (n):
        for j in range (0,i+1):
            print("*", end = "")
        print()

star_pyr(6)
num_pyr(6)
back_num_pyr(6)
back_star_pyr(6)
half_diamond(6)