j = 0
notfound = True

while notfound == True:
    j = j + 7
    for i in range(2,7):
        if j % i != 1:
            break
        elif i == 6:
            print (j)
            notfound = False
        else:
            continue