/*

Given an array with different numbers, return a new array with different subarrays containing identical numbers in the input

example:

  input: [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,5]

  output: [ [ 1, 1, 1, 1, 1, 1 ], [ 2, 2, 2, 2, 2 ], [ 3, 3, 3, 3 ], [ 4, 4 ], [ 5 ] ]
  
*/

function nest(array){
	
	array = array.sort();
	
	return array.reduce(function(a, b, i, v){

    	// it's different
    	if(v[i]!=v[i-1]){
    		var newItem = [[v[i]]];
    		return a.concat(newItem);	
    	}
    	
    	// it's the same
    	else{
    
    		var newVector = a;
    		newVector[newVector.length - 1] = newVector[newVector.length - 1].concat(v[i]);
    		return newVector;
    	}
    	
    	
    	},[]);
    	
	
}
