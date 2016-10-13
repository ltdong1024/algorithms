/*

  Function that takes an array and returns it reversed using .reduce method

*/



	  function reverse(array){

	    return array.reduce(function(inicial,act,i,arr){

	      return inicial.concat(arr[arr.length-1-i]);

	    },[])

	  }
	  
	  
////////// Version that accepts both arrays and strings:

	  function reverse(arg){
  
        // check if the argument is a string:
	  		return (arg+"" === arg) 
              // turn the array into a string, reverse it, and join back together.
	  				? arg.split("").reduce(function(inicial,act,i,arr){

		      					return inicial.concat(arr[arr.length-1-i]);

		    					},[]).join("")
		    					
              // reverse the array
	  				: arg.reduce(function(inicial,act,i,arr){

		     					return inicial.concat(arr[arr.length-1-i]);

		   						},[])

	  }
