'''
  from https://www.codewars.com/kata/525c65e51bf619685c000059/
  
  Return the máximum ammount of cakes that can be done
  with the available ingredients, given the recipe of the cake.
  
  Look for the most limiting ingredient in the list, 
  and return the multiple of the available ingredient 
  with respect the necessary ingredient.
  
'''

#example given arguments
recipe = {
	"flour": 500, 
	"sugar": 200, 
	"eggs": 1
	}
ingredients = {
	"flour": 1200, 
	"sugar": 1200, 
	"eggs": 5, 
	"milk": 200
	}

# try/except solution:
def cakes(rec, ing):
    ammount = []
    for key, value in rec.items():
        try:
            ammount.append(ing[key]//value)
        except:
            ammount.append(0)
    return min(ammount)

# list comprehension:
def cakes_succint(rec, ing):
	return min([ing.get(key,0)//value for key, value in rec.items()])
