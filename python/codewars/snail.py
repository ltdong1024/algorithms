'''
from https://www.codewars.com/kata/snail/

Given an n x n array, 
return the array elements arranged 
from outermost elements to the middle element, 
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
         
snail(array) #=> [1,2,3,6,9,8,7,4,5]

'''


def snail(array):
    
    n = len(array)
    
    if n == 1:
        return array[0]
    
    result = []
    
    while n>1:
        #A
        for i in array[0][0:]:
            result.append(i)
        array = array[1:]
        
        # B
        for i in range(0,n-1):
            result.append(array[i][-1])
            array[i] = array[i][:-1]

        # C
        for i in array[n-2][::-1]:
            result.append(i)
        array = array[:-1]
        
        # D
        for i in range(0,n-2)[::-1]:
            result.append(array[i][0])
            array[i] = array[i][1:]

        n = len(array)
    
    if len(array) == 1:
        result.append(array[0][0])

    return(result)
