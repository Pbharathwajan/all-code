numlist= [23,1,2,42,53,4,75,5,45,1353,57,5,32]
numlist.sort(reverse=True)
print (numlist)
num_1 = 23,1,2,42,53,4,75,5,45,1353,57,5,32
x = 0

print(f"The original Numbers are {numlist}")
print (len(numlist))

for i in range(0,len(numlist)-1):
    for j in range(i+1,len(numlist)):
        if numlist[i] > numlist[j] :
            x=numlist[j]
            numlist[j]= numlist[i]  
            numlist[i]=x

print(f"The numbers in ascending order:{numlist}")

numlist.sort(reverse=True)
print(f"The numbers in descending order:{numlist}")


    
    

    