from flask import Flask
from flask import request
import ctypes

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/simpleRes', methods=['GET','POST'])
def scalc():
	lib = ctypes.CDLL("./calcLib.so")
	lib.simpleCalc.restype = ctypes.c_float
	lib.simpleCalc.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_wchar]

	op1 = int(request.form.get('operand1'))
	op2 = int(request.form.get('operand2'))
	oper = request.form.get('operatorList')

	if (oper == "/"):
		val = str(round(lib.simpleCalc(op1, op2, oper), 5))
	else:
		val = str(int(lib.simpleCalc(op1, op2, oper)))
	return val

@app.route('/trigRes', methods=['GET','POST'])
def tcalc():
	lib = ctypes.CDLL("./calcLib.so")
	lib.angCalc.restype = ctypes.c_float
	lib.angCalc.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p]
	lib.sideCalc.restype = ctypes.c_float
	lib.sideCalc.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p]

	op1 = int(request.form.get('trigOp1'))
	op2 = int(request.form.get('trigOp2'))
	opType1 = request.form.get('trigList1')
	opType2 = request.form.get('trigList2')
	oper = request.form.get('trigOpList')
	func = request.form.get('trigFuncList')

	#Ran into issues comparing string with values after passing to C
	#The solution I found was to pass in single character pointers and use strcmp() to
	#compare, once passed to C.

	#This section makes values easier to compare, after being passed to the C function.
	#In order to figure out what kind of calculation needs to be done here.

	if (func == "Sin"):
		func = "s"
	if (func == "Cos"):
		func = "c"
	if (func == "Tan"):
		func = "t"

	if (opType1 == "Opposite Side"):
		opType1 = "o"
	if (opType1 == "Adjacent Side"):
		opType1 = "s"
	if (opType1 == "Angle(deg)"):
		opType1 = "a"

	if (opType2 == "Opposite Side"):
		opType2 = "o"
	if (opType2 == "Adjacent Side"):
		opType2 = "s"
	if (opType2 == "Angle(deg)"):
		opType2 = "a"
	if (opType2 == "Hypotenuse"):
		opType2 = "h"
	

	#Some catches for nonsensical inputs have been added, but I have not
	#put much thought into it.

	if (opType1 == "a") and (opType2 == "a"):
		return "Invalid Operands"
	if (opType1 == "o") and (opType2 == "o"):
		return "Invalid Operands"
	if (opType1 == "s") and (opType2 == "s"):
		return "Invalid Operands"
	if (opType1 == "h") and (opType2 == "h"):
		return "Invalid Operands"


	if (oper == "Find Angle"):
		val = str(round(lib.angCalc(op1, op2, opType1, opType2, func), 2))
	else:
		val = str(round(lib.sideCalc(op1, op2, opType1, opType2, func), 4))

	#The temporary error code is the string "383.0".
	#This will cause "383.0" to be recognized as an error, even if correct.
	#This will be changed in the future in order to allow 383 as a result.

	if (val == "383.0"):
		val = "Invalid Input. Please double-check and try again."

	return val

if __name__ == '__main__':
	app.run(
		host="0.0.0.0",
		port=8080
	)
