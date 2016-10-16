'''
based on a Polish computer game
turn numbers from base 10 to base-2
and from base-2 to base 10

from https://www.codewars.com/kata/skrzat/

'''

def int_to_bin(number):
    if number == 0:
        return "0"
    binary = []
    while number != 0:
        number, remainder = divmod(number, -2)
        if remainder < 0:
            number, remainder = number + 1, remainder + 2     
        binary.append(str(remainder))
    return "".join(binary[::-1])

def bin_to_int(b):
    return sum([int(b[::-1][i]) * pow(-2,i) for i in range(len(b))]) 


def skrzat(base, number):
    print(number)
    if base == "b":
        base = "binary"
        result = bin_to_int(number)

    if base == "d":
        base = "decimal"
        result = int_to_bin(number)
    print(result)
    return "From {}: {} is {}".format(base,number,result)
