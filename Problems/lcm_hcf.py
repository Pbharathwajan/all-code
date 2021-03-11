
def hcf_lcm(num1,num2):

    temp = 0
    x,y= max(num1,num2), min(num1,num2) 

    while y > 0:
        temp = y
        y = x % y
        x = temp

    print(f"The HCF of {num1} and {num2} is {x}!")
    print(f"The LCM of {num1} and {num2} is {(num1*num2)/x}!")

def lcm()


    
hcf_lcm(54,24)

