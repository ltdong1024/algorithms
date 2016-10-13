/*

  This function finds an element in an object and returns the first key that element belongs to

*/

function findInObject(value,obj){
	
	var keys = Object.keys(obj)
	
	for(var k in keys){
		
		if(obj[keys[k]].indexOf(value) != -1) return keys[k]
		
	}
	
}





/// EXAMPLE:



var errorTypes = {

	// no error to show
	0 : [1],

	// combinable
	1 : [2,3],

	// issues
	2: [4],

	// non-combinable
	3: [5,6]

};


var ex = 2;




findInObject(ex,errorTypes)
