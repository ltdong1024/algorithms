'''
'''


import re



# compact
def solution(string,markers):
    return "\n".join([re.split("|".join(["\\{}".format(marker) for marker in markers]), line)[0].strip() for line in string.split("\n")])
    

# detailed
def detailed_solution(string,markers):
    # rearrange the markers
    markers = ["\\{}".format(marker) for marker in markers]
    
    # put markers together in a regex pattern, separated by "|"
    re_markers = "|".join(markers)
    
    # separate the string into lines
    lines = string.split("\n")
    
    # split every line by markers, and take the first element; trim spaces with strip()
    new_lines = [re.split(re_markers, line)[0].strip() for line in lines]
    
    #return the new lines put back together
    return "\n".join(new_lines)
