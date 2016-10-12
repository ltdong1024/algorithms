'''
from:

Given a pair of selectors in CSS, returns the one with more priority
The logic is as follows:

0 "*" selector is the last one
1 Selector with more #id selectors wins
2 If both are same, the winner is selector with more .class selectors
3 If both are same, selector with more elements wins
4 If all of above values are same, the winner is selector that appear last

'''

import re

def compare(a, b):
  #Selector with more #id selectors wins
  a_id = len([x for x in a.split("#")])
  b_id = len([x for x in b.split("#")])
  if a_id > b_id:
    return a
  if b_id > a_id:
    return b
  #Selector with more .class selectors wins
  a_class = len([x for x in a.split(".")])
  b_class = len([x for x in b.split(".")])
  if a_class > b_class:
    return a
  if b_class > a_class:
    return b
    
  #If both are same, selector with more elements wins
  a_all = len([x for x in re.split(r'\#|\.|\s',a) if x!=""])
  b_all = len([x for x in re.split(r'\#|\.|\s',b) if x!=""])
  if a_all > b_all:
    return a
  if b_all > a_all:
    return b
  
  #finally, return the last element, unless is "*"
  if b != "*":
    return b
  else:
    return a
