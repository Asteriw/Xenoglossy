function popList() {

	//Simple Calculator section

	var operatorObjects = ["+","-","*","/"];
	var simpElem = document.getElementById("operatorList")
	for (var i = 0; i < operatorObjects.length; i++) {
		simpElem.options[i] = new Option(operatorObjects[i], operatorObjects[i]);
  	}

  	//Trig Calculator section

  	var trigObjects1 = ["Opposite Side", "Adjacent Side", "Angle(deg)"]
  	var trigObjects2 = ["Opposite Side", "Adjacent Side", "Hypotenuse", "Angle(deg)"]

  	var trigElem1 = document.getElementById("trigList1")
  	var trigElem2 = document.getElementById("trigList2")

  	for (var i = 0; i < trigObjects1.length; i++) {
		trigElem1.options[i] = new Option(trigObjects1[i], trigObjects1[i]);
  	}
  	for (var i = 0; i < trigObjects2.length; i++) {
		trigElem2.options[i] = new Option(trigObjects2[i], trigObjects2[i]);
  	}

  	var trigOpObjects = ["Find Side","Find Angle"];
	var trigElem = document.getElementById("trigOpList")
	for (var i = 0; i < trigOpObjects.length; i++) {
		trigElem.options[i] = new Option(trigOpObjects[i], trigOpObjects[i]);
  	}

  	var trigFuncObjects = ["Sin", "Cos", "Tan"];
	var trigFuncElem = document.getElementById("trigFuncList")
	for (var i = 0; i < trigFuncObjects.length; i++) {
		trigFuncElem.options[i] = new Option(trigFuncObjects[i], trigFuncObjects[i]);
  	}

  	//The below commented out code was originally intended to populate the elements
  	//in two dropdown lists. The second list's options were intended to update and change
  	//depending on which option was selected in the first dropdown. Unfortunately, this
  	//functionality did not make it into the final version prior to my deadline.

  	// var inType = {
  	// 	"Side": ["Hypotenuse", "Angle"],
  	// 	"Angle": ["Side"]
  	// }
  	// var trigElem1 = document.getElementById("trigOp1")
  	// var trigElem2 = document.getElementById("trigOp2")
  	// for (var x in inType) {
  	// 	trigElem1.options[trigElem1.options.length] = new Option(x, x);
  	// }
  	// trigElem1.onchange = function() {
  	// 	trigElem2.length = 1;
  	// 	for (var y in subjectObject[this.value]) {
   //    		trigElem2.options[trigElem2.options.length] = new Option(y, y);
   //  	}
  	// }
}

//The Bundler function was originally intended to bundle form data into JSON
//but I decided not to use JSON.

function bundler() {
	var op1 = document.getElementById("operand1").value;
	var op2 = document.getElementById("operand2").value;
	var operator = document.getElementById("operatorList").value;
	var operation = {"op1":op1, "op2":op2, "operator":operator};
	var opJSON = JSON.stringify(operation);
	alert(operation);
}

//The Tester function exists to test HTML and JS funcionality, and also to check values.

function tester() {
	var testVal = document.getElementById("operatorList").value;
	alert(typeof testVal)
}