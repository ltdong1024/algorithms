'''
Function to turn binary into integer numbers
'''

# detailed version
def bin_to_int_detailed(b):
  # reverse the string containing the binary number
  bin = bin[::-1]
  
	integer = 0
	
  # for every 1/0 in the binary number add the power of two corresponding to its position
  for i in range(len(bin)):
		integer += int(bin[i]) * pow(2,i)
    
	return integer
  
  
# using list comprehension
def bin_to_int(b):
	return sum([int(b[::-1][i]) * pow(2,i) for i in range(len(b))]) 
