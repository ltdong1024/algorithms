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
    
    max_power = int(math.log(n,2) + 1)
    powers = [pow(2,i) for i in range(max_power)][::-1]

    binary = ""
    for i in powers:
        w = math.floor(n//i)
        n = n - w*i
        binary += str(int(w))
    
    binary = "0"*(min_length-len(binary)) + binary

    return binary
