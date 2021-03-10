syscon = input("Enter system to convert from: ")
systo = input("Enter system to convert to: ")
n = int(input("Enter number here: "))



def bin_to_bin():
    print (bin(int(str(n), 2)))


def bin_to_dec():
    print (int(str(n), 2))


def bin_to_oct():
    print (oct(int(str(n), 2)))


def bin_to_hex():
    print (hex(int(str(n), 2)))


def dec_to_bin():
    print (bin(int(n)))


def dec_to_dec():
    print (int(n))


def dec_to_oct():
    print (oct(int(n)))


def dec_to_hex():
    print (hex(int(n)))


def oct_to_bin():
    print (bin(int(str(n), 8)))


def oct_to_dec():
    print (int(str(n), 8))


def oct_to_oct():
    print (oct(int(str(n), 8)))


def oct_to_hex():
    print (hex(int(str(n), 8)))


def hex_to_bin():
    print (bin(int(str(n), 16)))


def hex_to_dec():
    print (int(str(n), 16))


def hex_to_oct():
    print (oct(int(str(n), 16)))


def hex_to_hex():
    print (hex(int(str(n), 16)))
    

#INPUT
if syscon == "bin" and systo == "bin":
    bin_to_bin()

if syscon == "bin" and systo == "dec":
    bin_to_dec()

if syscon == "bin" and systo == "hex":
    bin_to_hex()

if syscon == "bin" and systo == "oct":
    bin_to_oct()

if syscon == "dec" and systo == "bin":
    dec_to_bin()

if syscon == "dec" and systo == "dec":
    dec_to_dec()

if syscon == "dec" and systo == "hex":
    dec_to_hex()

if syscon == "dec" and systo == "oct":
    dec_to_oct()

if syscon == "hex" and systo == "bin":
    hex_to_bin()

if syscon == "hex" and systo == "dec":
    hex_to_dec()

if syscon == "hex" and systo == "hex":
    hex_to_hex()

if syscon == "hex" and systo == "oct":
    hex_to_oct()

if syscon == "oct" and systo == "bin":
    oct_to_bin()

if syscon == "oct" and systo == "dec":
    oct_to_dec()

if syscon == "oct" and systo == "hex":
    oct_to_hex()

if syscon == "oct" and systo == "oct":
    oct_to_oct()
    
    