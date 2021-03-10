G = input("Enter system to convert to: ")



def todec():
    E = input("Enter system to convert from: ")
    n = (input("Enter number here: "))



    def bintodec():
        print(int(n, base = 2))

    def hextodec():
        print(int(n,base = 16))

    def octtodec():
        print(int(n,base = 8))


    if E == "binary":
        bintodec()

    if E == "hexadecimal":
        hextodec()

    if E == "octal":
        octtodec()ch


def tobin():
    E = input("Enter system to convert from: ")
    
    def fromhex():
        n = input("Enter number: ")
        
        n = int(n,16)
        
        print(bin(n))
        
        
        
    def fromoct():
        n = input("Enter number: ")
        
        n = int(n,8)
        
        print(bin(n))

    def fromdec():
        n = int(input("Enter number: "))
        
        print(bin(n))
        
    if E == "hexadecimal":
        fromhex()
        
    if E == "octal":
        fromoct()
        
    if E == "decimal":
        fromdec()
    


def tooct():
    E = input("Enter system to convert from: ")
    
    def fromdec():
        n = int(input("Enter number: "))
        
        print(oct(n))
        
    def frombin():
        n = input("Enter number: ")
        
        n = int(n,2)
        
        print(oct(n))
    
    def fromhex():
        n = input("Enter number: ")
        
        n = int(n,16)
        
        print(oct(n))
    
    if E == "decimal":
        fromdec()
        
    if E == "hexadecimal":
        fromhex()
        
    if E == "binary":
        frombin()

def tohex():
    E = input("Enter system to convert from: ")
    
    def frombin():
        n = input("Enter number: ")
        
        n = int(n,2)
        
        print(hex(n))
    
    def fromoct():
        n = input("Enter number: ")
        
        n = int(n,8)
        
        print(n)
        
        
    def fromdec():
        n = int(input("Enter number: "))
        
        print(hex(n))
    
    if E == "decimal":
        fromdec()
    
    if E == "octal":
        fromoct()
        
    if E == "binary":
        frombin()
        
        
        
if G == "decimal":
    todec()
    
if G == "octal":
    tooct()
    
if G == "hexadecimal":
    tohex()
    
if G == "binary":
    tobin()
    

