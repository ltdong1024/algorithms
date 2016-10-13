	/*
	
	This function returns a random element inside an array:
	
	*/
	
	
	function randomElement(arr){

		var len = arr.length;

		var randomInRange = Math.random()*len;

		var randomIndex = Math.floor(randomInRange);

		return arr[randomIndex];

	}
