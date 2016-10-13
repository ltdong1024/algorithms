
// count length of a number

	function countDigits(n){

	  var radix = 1;
	  while(n >= Math.pow(10,radix)){
	    radix++;
	  }
	  return radix;

	}

	// or: (less precise)
	// be careful with negative numbers
	function len(n){
 		return Math.ceil(Math.log(n + 1) / Math.LN10);
 	}
