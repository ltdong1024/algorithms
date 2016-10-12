'''
function to turn integers into binary numbers.
It allows the user to especify the min length
of the binary number, adding 0's if necessary.

it requires math
'''

import math

def int_to_bin(n, min_length=8):
    if n == 0:
        return "0"*min_length
    if n == 1:
        return "0"*(min_length - 1) + "1"
    if n == 2:
        return "0"*(min_length - 2) + "10"
    
    max_power = int(math.ceil(math.log(n,2)))
    powers = [pow(2,i) for i in range(max_power)][::-1]

    binary = ""
    for i in powers:
        w = math.floor(n//i)
        n = n - w*i
        binary += str(int(w))
    
    binary = "0"*(min_length-len(binary)) + binary

    return binary
