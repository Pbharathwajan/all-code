x = [1,2,3,4,5,5,6]
greatest = x[0] #Placeholder
secgreat = x[1]
for i in range (len(x)):
    if x[i] > greatest: #checks if x[i] is greater than greatest, if it is - 
        secgreat = greatest #greatest becomes second greatest
        greatest = x[i] #x[i] becomes the greatest
    elif x[i] < greatest and x[i] > secgreat:
        secgreat = x[i]


print (secgreat)
print (greatest)