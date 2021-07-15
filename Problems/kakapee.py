


def numpat(num):
    for i in range (num):
        for j in range (0,i+1):
            print(j,end ='')
            num = (num+1)
    print("\r")

numpat(6)
