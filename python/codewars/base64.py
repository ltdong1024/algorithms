'''
from:
from:

left: solve tailing "A" on base 64
'''



import math

def int_to_bin(n, min_length=8):
    if n == 0:
        return "0"*min_length

    max_power = int(math.log(n,2) + 1)
    powers = [pow(2,i) for i in range(max_power)][::-1]

    binary = ""
    for i in powers:
        w = math.floor(n//i)
        n = n%i
        binary += str(int(w))
    
    binary = "0"*(min_length-len(binary)) + binary

    return binary


def bin_to_int(b):
    return sum([int(b[::-1][i]) * pow(2,i) for i in range(len(b))]) 

def int_to_base64(int):
    # from 0 to 25 is A to Z
    if int in range(26):
        return chr(int + 65)
    # from 26 to 51 is a to z
    if int in range(26, 52):
        return chr(int + 71)
    # from 52 to 61 is 0 to 9
    if int in range(52, 62):
        return chr(int - 4)

    # other cases
    if int == 62:
        return "+"
    if int == 63:
        return "/"

def base64_to_int(base64):

    # from A to Z is 0-25
    if ord(base64) - 65 in range(26):
        return ord(base64) - 65
    # from a to z is 26-51
    if ord(base64) - 71 in range(26, 52):
        return ord(base64) - 71 
    # from 0 to 9 is 52-61
    if ord(base64) + 4 in range(52, 62):
        return ord(base64) + 4

    # other cases
    if base64 == "+":
        return 62
    if base64 == "/":
        return 63

def to_base_64(str):
    # turn every letter in the string into a binary and add them together
    binaries = "".join([int_to_bin(ord(char)) for char in str])

    # add zeroes until reaching 24 characters
    binaries += "0"*(24 - len(binaries)%24)

    # split every 6 characters
    binaries = [binaries[i:i+6] for i in range(0,len(binaries),6)]

    # turn every binary into a number
    base64 = "".join([int_to_base64(bin_to_int(binary)) for binary in binaries])

    # trim tailing "A"
    while base64[-1] == "A":
        base64 = base64[:-1]

    return base64

def from_base_64(base64):
    # add "A" if necessary
    base64 += "A"*(6 - len(base64)%6)

    # turn every char into a binary number
    binaries = "".join([int_to_bin(base64_to_int(char), min_length=6) for char in base64])

    # split every 8 characters
    binaries = [binaries[i:i+8] for i in range(0,len(binaries),8)]

    # turn into integers
    integers = [bin_to_int(i) for i in binaries]

    # trim tailing 0s
    while integers[-1] == 0:
        integers = integers[:-1]

    # turn every binary number into a char
    string = "".join([chr(i) for i in integers])

    return string

