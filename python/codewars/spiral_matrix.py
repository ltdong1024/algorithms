'''

for a given size, creates an spiral matrix

size 10:

[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
[1, 0, 1, 1, 1, 1, 0, 1, 0, 1]
[1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
[1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


from: https://www.codewars.com/kata/make-a-spiral/

'''

def spiralize(size):
    # handle 0 matrices
    if size == 0:
        return []
    
    # create an empty matrix
    matrix = [[0 for i in range(size)] for i in range(size)]
    
    # initialize start-end points
    initial = - 2        # offset to start on 0
    final = size + 2
    
    for i in range(size*4):

        if i%4 == 0: # up
            # set start-end points 
            final -= 2
            initial += 2

            ran = range(initial - 1, final)

            for j in ran:
                matrix[initial][j] = 1

        if i%4 == 1:  # right
            ran = range(initial, final)
            for j in ran:
                matrix[j][final-1] = 1

        if i%4 == 2:  # bottom
            ran = range(initial, final)
            for j in ran:
                matrix[final-1][j] = 1

        if i%4 == 3:  # left
            ran = range(initial + 2, final)
            for j in ran:
                matrix[j][initial] = 1
    
        # exit
        if len(ran) <= 2:
            return matrix
